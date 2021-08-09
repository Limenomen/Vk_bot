from logging import error
import requests
from vk_api import longpoll
from vk_api.bot_longpoll import VkBotEventType
from settings import api_key, group_id
import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from plugins.base_plugin import Plugin
from plugins.plugin_list import plugin_list
from re import match


class vk_bot():
    def __init__(self, api_key):
        self.vk_session = vk_api.VkApi(token=api_key)
        self.vk = self.vk_session.get_api()
        self.longpoll = VkBotLongPoll(self.vk_session, group_id=group_id)
        self.plugins = plugin_list()
        self.listen()

    def listen(self):
        """
        Прослушивание longpoll сервера, принимает события
        """
        while True:
            try:
                for event in self.longpoll.listen():
                    self.event_handler(event)
            except requests.exceptions.ConnectionError as e:
                print(f'ошибка: {e}, переподключаюсь')
                self.reconnection()

    def event_handler(self, event):
        """
        обработчик событий
        """
        if event.type == VkBotEventType.MESSAGE_NEW:
            self.message_event_handler(event)

    def message_event_handler(self, event):
        """
        Обработчик события входящего сообщения
        """
        user_id = event.obj.peer_id
        message_text = event.obj.text

        # Находим слово-команду в начале строки:
        plugin = None
        try:
            plugin = next(
                plugin
                for plugin in self.plugins
                for command in plugin.get_commands().split("|")
                if match(rf"{command}", message_text.lower())
            )
        except Exception as e:
            self.send_message(user_id, "Извините, такой команды пока нет(.")
        if plugin:
            self.plugin_starter(plugin, event)

    def plugin_starter(self, plugin, event):
        """
        метод для запуска плагинов
        """
        input = event.obj.text.lower()
        for command in plugin.get_commands().split("|"):
            if match(rf"{command}", input):
                input = input.replace(f'{command}', '')
        input = input.replace(' ', '')
        self.send_message(event.obj.peer_id, plugin.start(input))
        pass

    def send_message(self, user_id, message):
        """
        Функция для отправки сообщения
        """
        self.vk.messages.send(
            user_id=user_id, message=message, random_id=get_random_id())

    def reconnection(self):
        self.longpoll = VkBotLongPoll(self.vk_session, group_id=group_id)
        pass


def main():
    bot = vk_bot(api_key=api_key)
    


if __name__ == "__main__":
    main()

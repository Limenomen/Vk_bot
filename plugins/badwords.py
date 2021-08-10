from plugins.base_plugin import Plugin
from codecs import open
from random import randint
from re import match, search


class badwords_plugin(Plugin):
    __plugin_name__ = "chat"
    badwords = []
    def __init__(self):
        with open('plugins//badwords.txt', 'r', 'utf-8') as badwords:
            self.badwords = list(str(badwords.read()).split(', '))
            pass

    def start(self, text):
        text = str(text)
        for word in self.badwords:
            if search(rf"{word}", text):
                answer_list = ["Сам такой!!!", "нет, ты!", "а может это ты такой?", "ну ты дурак конечно.", "больше не пиши сюда.", "мда", "по другому не скажешь.", "а кому сейчас легко?", "фу"]
                random = randint(0, len(answer_list)-1)
                return (answer_list[random])
        else:
            return("Извините, такой команды пока нет(.")

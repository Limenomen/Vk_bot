from plugins.base_plugin import Plugin
from codecs import open
from random import randint


class badwords_plugin(Plugin):
    __plugin_name__ = "chat"
    badwords = tuple()
    def __init__(self):
        with open('plugins//badwords.txt', 'r', 'utf-8') as badwords:
            self.badwords = tuple(badwords.read().split(', '))
            pass

    def start(self, text):
        
        if text in self.badwords:
            answer_list = ["Сам такой!!!", "нет, ты!", "а может это ты такой?", "ну ты дурак конечно.", "больше не пиши сюда.", "мда", "по другому не скажешь.", "а кому сейчас легко?", "фу"]
            random = randint(0, len(answer_list)-1)
            return (answer_list[random])
        else:
            return("Извините, такой команды пока нет(.")

from plugins.base_plugin import Plugin
import requests
from plugins.base_plugin import Plugin
import re
from threading import current_thread

class WeatherPlugin(Plugin):
    __plugin_name__ = "weather"
    __plugin_commands__ = ('погода в', 'погода')
    API_key = "f3a700d25f54653a8dea83dc569c11ab"
    
    def __init__(self):
        Plugin.__init__(self)

    def start(self, message_text):
        City_name = message_text
        try:
            result = requests.get("http://api.openweathermap.org/data/2.5/weather",
                                params={'q': City_name, 'APPID': self.API_key, 'lang': 'ru', 'units':'metric'})
            result.raise_for_status()
        except requests.exceptions.RequestException as e:
            return "Извините, что-то пошло не так. Попробуйте еще раз."

        data = result.json()
        temperature = data['main'].get('temp')
        sky = data['weather'][0].get('description')
        #print(current_thread())
        return(f"температура в городе {data['name']} сейчас: {temperature:.01f}, {sky}")

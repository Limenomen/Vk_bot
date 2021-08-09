from plugins.base_plugin import Plugin
from plugins.weather import weather_plugin

def plugin_list() -> list:
    
    plugin_list = [subclass() for subclass in Plugin.__subclasses__()]
    return plugin_list
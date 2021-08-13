class Plugin():
    """
    Базовый шаблон для плагинов
    """
    __plugin_name__ = str()
    __plugin_commands__ = tuple()

    def __init__(self):
        pass

    def start(self, *args, **kwargs):
        pass

    def get_commands(self):
        return "|".join(self.__plugin_commands__)





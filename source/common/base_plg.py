from yapsy.IPlugin import IPlugin

class IBasePlugin(IPlugin):
    def get_name(self):
        return "IBasePlugin"

    def set_plugin_manager(self, manager):
        self._plugin_manager = manager
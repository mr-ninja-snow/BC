import sys
sys.path.append("../../")
from common.base_plg import IBasePlugin

from common.log_plg.message_level import MessageLevels

class ILogicPlugin(IBasePlugin):
    def get_name(self):
        return "ILogicPlugin"

    LOG_INFO_MESSAGE_INIT = "the plugin was inited"
    LOG_INFO_MESSAGE_START = "the plugin was started"
    LOG_INFO_MESSAGE_STOPED = "the plugin was stoped"
    LOG_INFO_MESSAGE_FINISH = "the plugin finished executing"

    def init(self):

        self.register_log_messages()

        # Trigger 'some action' from the "Visualization" plugins
        print(self._plugin_manager.getPluginByName('Text Local Logging', 'Logging').plugin_object)
        # for pluginInfo in manager.getPluginsOfCategory("Logging"):
        #     pluginInfo.plugin_object.register_module_messages("", "")
        # .getPluginByName()

    def register_log_messages(self):
        self._log_messages = list()
        self._log_messages.append({"text": LOG_INFO_MESSAGE_INIT, "level": MessageLevels.INFO})
        

    def start(self):
        pass

    def stop(self):
        pass

    def finish(self):
        pass
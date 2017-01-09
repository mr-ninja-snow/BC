import sys
sys.path.append("../../")
from common.BasePlg import IBasePlugin

from common.log_plg.MessageLevels import MessageLevels

class ILogicPlugin(IBasePlugin):
	def get_name(self):
		return "ILogicPlugin"

	LOG_INFO_MESSAGE_INIT = { "text": "the plugin was inited", "id" : -1}
	LOG_INFO_MESSAGE_START = { "text": "the plugin was started", "id" : -1}
	LOG_INFO_MESSAGE_STOPED = { "text": "the plugin was stoped", "id" : -1}
	LOG_INFO_MESSAGE_FINISH = { "text": "the plugin finished executing", "id" : -1}

	def init(self):

		self.register_log_messages()

		# Trigger 'some action' from the "Visualization" plugins
		# print(self._plugin_manager.getPluginByName('Text Local Logging', 'Logging').plugin_object)
		# for pluginInfo in manager.getPluginsOfCategory("Logging"):
		#     pluginInfo.plugin_object.register_module_messages("", "")
		# .getPluginByName()

	def register_log_messages(self):
		self._log_messages = list()
		self._log_messages.append({"text": ILogicPlugin.LOG_INFO_MESSAGE_INIT["text"], "level": MessageLevels.INFO})
		ILogicPlugin.LOG_INFO_MESSAGE_INIT["id"] = len(self._log_messages) - 1

		self._log_messages.append({"text": ILogicPlugin.LOG_INFO_MESSAGE_START["text"], "level": MessageLevels.INFO})
		ILogicPlugin.LOG_INFO_MESSAGE_START["id"] = len(self._log_messages) - 1

		self._log_messages.append({"text": ILogicPlugin.LOG_INFO_MESSAGE_STOPED["text"], "level": MessageLevels.INFO})
		ILogicPlugin.LOG_INFO_MESSAGE_STOPED["id"] = len(self._log_messages) - 1

		self._log_messages.append({"text": ILogicPlugin.LOG_INFO_MESSAGE_FINISH["text"], "level": MessageLevels.INFO})
		ILogicPlugin.LOG_INFO_MESSAGE_FINISH["id"] = len(self._log_messages) - 1

		self._plugin_manager.getPluginByName('Text Local Logging', 'Logging').plugin_object.register_module_messages(self.get_name(), self._log_messages)

	def start(self):
		pass

	def stop(self):
		pass

	def finish(self):
		pass
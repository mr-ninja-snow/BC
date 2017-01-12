from common.log_plg.ILogPlg import ILogPlugin

from common.log_plg.MessageLevels import MessageLevels

class Logging(ILogPlugin):

	LOG_INFO_MESSAGE_REGISTER = {"text": "registering log messages for %%", "id": -1}

	# __EXEC_MODE = "Production"
	__EXEC_MODE = "Local debug"

	def __init__(self):
		super().__init__()

		self._log_messages = list()
		self._log_messages.append(
			{"text": Logging.LOG_INFO_MESSAGE_REGISTER["text"], "level": MessageLevels.INFO})
		Logging.LOG_INFO_MESSAGE_REGISTER["id"] = len(self._log_messages) - 1

		self.__plugin_message_dict = dict()
		self.__plugin_message_dict["Logging"] = self._log_messages

	def get_name(self):
		return "Logging"

	def register_module_messages(self, module_name, module_messages):
		self.__plugin_message_dict[module_name] = module_messages

		self.log(self.get_name(), Logging.LOG_INFO_MESSAGE_REGISTER["id"], [module_name])

	def log(self, module_name, message_index, extra_args = []):
		import datetime
		import time
		ts = time.time()
		time_stamp = datetime.datetime.fromtimestamp(ts).strftime('%m.%d %H:%M:%S')

		log_line = time_stamp + ' ' + module_name + ' '

		def get_msg_prefix(x):
			return {
				MessageLevels.DEBUG: 'DBG',
				MessageLevels.INFO: 'INF',
				MessageLevels.WARNING: 'WRNG',
				MessageLevels.ERROR: 'ERR',
				MessageLevels.FATAL_ERROR: 'FATALERR',
			}[x]

		log_line += get_msg_prefix(self.__plugin_message_dict[module_name][message_index]["level"]) + ":"

		if len(extra_args):
			import re
			msg = self.__plugin_message_dict[module_name][message_index]['text']
			for arg in extra_args:
				msg = re.sub(r"%%", arg, msg, 1)
			log_line += msg
		else:
			log_line += self.__plugin_message_dict[module_name][message_index]['text']


		if Logging.__EXEC_MODE != "Local debug":
			pass
			# write to rolling log
		else:
			print(log_line)
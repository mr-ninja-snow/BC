#!/usr/bin/python3

import sys
sys.path.append("../../")
from common.BasePlg import IBasePlugin

class ILogPlugin(IBasePlugin):

	def get_name(self):
		return "ILogPlugin"

	def register_module_messages(self, module_name, module_messages):
		pass

	def log(self, module_name, message_index):
		pass
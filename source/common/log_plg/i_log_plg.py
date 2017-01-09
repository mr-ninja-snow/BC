#!/usr/bin/python3

import sys
sys.path.append("../../")
from common.base_plg import IBasePlugin

class ILogPlugin(IBasePlugin):
    def get_name(self):
        return "ILogPlugin"

    def register_module_messages(self, module_name, module_messages):
        print("register module messages")

    def log(self, message_level, module_name, message_index):
        print("log")
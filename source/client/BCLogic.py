#!/usr/bin/python3

import sys
sys.path.append("../")
from common.LogicPlg import ILogicPlugin

class BCLogic(ILogicPlugin):
    def init(self):
        ILogicPlugin.init(self)
        # Trigger 'some action' from the "Visualization" plugins

        # for pluginInfo in self._plugin_manager.getPluginsOfCategory("Logging"):
        #     pluginInfo.plugin_object.register_module_messages("", "")

        # Load the plugins from the plugin directory.
        # manager = PluginManager()
        # manager.setPluginPlaces(["../common/log_plg/"])
        # manager.setCategoriesFilter({
        #    "Logging" : ILogPlugin,
        #    })

        # manager.collectPlugins()

        # # Trigger 'some action' from the "Visualization" plugins
        # for pluginInfo in manager.getPluginsOfCategory("Logging"):
        #     # print(str(pluginInfo))
        #     print(pluginInfo.plugin_object.get_name())
        #     # pluginInfo.plugin_object.register_module_messages("", "")
    
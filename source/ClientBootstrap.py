#!/usr/bin/python3

from yapsy.PluginManager import PluginManager

from common.log_plg.ILogPlg import ILogPlugin
from common.LogicPlg import ILogicPlugin

def main():
    # Load the plugins from the plugin directory.
    manager = PluginManager()
    manager.setPluginPlaces(["client/", "common/log_plg/"])
    manager.setCategoriesFilter({
       "Logging" : ILogPlugin,
       "Logic" : ILogicPlugin,
       })

    manager.collectPlugins()


    # # Loop round the plugins and print their names.
    for plugin in manager.getAllPlugins():
        print(plugin.plugin_object.get_name())
        plugin.plugin_object.set_plugin_manager(manager)

    manager.getPluginByName('BC Logic', 'Logic').plugin_object.init()


if __name__ == "__main__":
    main()
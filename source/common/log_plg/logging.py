from common.log_plg.i_log_plg import ILogPlugin

class Logging(ILogPlugin):
    def get_name(self):
        return "Logging"
import os
from ConfigParser import SafeConfigParser


class ConfigReader:
    def __init__(self):
        self.sections = ["user", "default"]
        self.config = SafeConfigParser()
        self.configdir = os.path.dirname(os.path.realpath(__file__))+"/../config/"
        self.config.read(self.configdir+"config.ini")
        sections = self.config.sections()
        if(not self.sections[0] in sections or not self.sections[1] in sections):
            self.error("Error in config file missing section " +
                       self.sections[0] + " or " + self.sections[1])

    def read(self, config_item):
        if(self.config.has_option("user", config_item)):
            return self.config.get("user", config_item)
        elif(self.config.has_option("default", config_item)):
            return self.config.get("default", config_item)
        else:
            self.error("Error option " + config_item +
                       " not found in config file.")

    def error(self, msg):
        print msg

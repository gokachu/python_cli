import ConfigParser

print config.sections()

print config.get("DEFAULT","HOME")

print config.get("USER","HOME")
def ConfigReader:
    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read("./config/config.ini")
        sections = self.config.sections()
        if(!"USER" in sections || !"DEFAULT" in sections):
                print("Error in config file missing section USER or DEFAULT")

    def read(config_item):
        self.config.get("USER",config_item);


return ConfigReader()

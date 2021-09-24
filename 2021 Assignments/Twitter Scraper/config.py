from configparser import ConfigParser

class ConfigFile():

    config_file = "config.ini"
    config = ConfigParser()
    data = config.read(config_file)
    


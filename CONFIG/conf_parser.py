import configparser
#==============================================================
Config = configparser.ConfigParser()
Config.read("CONFIG/config.ini")
#==============================================================

def do(section):
    #==============================================================
    #Get configuration parameters from the config.ini.
    #==============================================================
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1
    #==============================================================
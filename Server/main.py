"""A Minecraft server in python 3"""
# IMPORTS
from classes.server import MinecraftServer as Server

# INDICATIVE INFO DON'T TOUCH
# the version of this app. Don't touch this, it is for debug info
VERSION = "Alpha-dev"
# the Minecraft version. don't touch except if the protocoo of your version is the same as the MC version 1.17.1
CLIENT_VERSION = "1.17.1"

# MAIN
if __name__ == "__main__":
    print("""
    _________________________________________________
                Minecraft server in Python 3
                    Created by FewerElk
                   (github.com/FewerElk)
    If you have an issue please report it in GitHub !
    I decline all responsabilities when hacking, I'm
              not an expert in cyber-security !
    _________________________________________________
    """)
    print("Server version : {0}\nClients version : {1}".format(VERSION, CLIENT_VERSION))
    mc_server = Server(CLIENT_VERSION)
    mc_server.start()
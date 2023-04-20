"""A Minecraft server in python 3"""
from classes.server import MinecraftServer as Server

VERSION = "Alpha-dev"
CLIENT_VERSION = "1.19.4"

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
    mc_server = Server()
    mc_server.start()
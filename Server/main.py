"""A Minecraft server in python 3"""
from classes.server.server import MinecraftServer as Server

if __name__ == "__main__":
    print("""
    _________________________________________________
                Minecraft server in Python 3
                    Created by FewerElk
                   (github.com/FewerElk)
    If you have an issue please report it in GitHub !
    _________________________________________________
    """)
    print("Launching Minecraft server...")
    mc_server = Server()
    mc_server.start()
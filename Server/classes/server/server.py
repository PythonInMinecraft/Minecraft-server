"""In this file, there is the class of the server thread"""
from time import *
from threading import Thread

class MinecraftServer(object):
    """Class of the Minecraft server"""
    def __init__(self, ip=("", 25565)):
        """Constructor"""
        ...
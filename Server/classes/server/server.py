"""In this file, there is the class of the server thread"""
from time import *
from threading import Thread
from socket_classes import *

class MinecraftServer(object):
    """Class of the Minecraft server"""
    def __init__(self, addr=socket.gethostname()):
        """Constructor
        Arg:
        - addr : the address (default is localhost)"""
        self.addr = (addr, 25565)   #Creating normal socket addr format
        self.socket = MinecraftSocketServerGestionner(addr=self.addr, port=25565)

    def start(self):
        """Launch the server"""
        ...
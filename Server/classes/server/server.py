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
        self.load_world()

    def load_world(self):
        """Load the worlds of the server
        THIS SECTION MUST HAVE CONTRIBUTORS !"""

    def open(self):
        """Open the server to clients"""
        self.socket.bind()
        

#class Listener(object):
#    """The listener of the server"""
#    LISTEN = False
#
#    def start(self):
#        """Start listening"""
#        self.LISTEN = True
#
#    def stop(self):
#        """Stop listening"""
#        self.LISTEN = False
#
#    def event(self, event):
#        """???"""


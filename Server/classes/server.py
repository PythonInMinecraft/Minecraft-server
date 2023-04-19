"""In this file, there is the class of the server thread"""
"""
#################################################
#################################################
############# HELP WANTED #######################
#################################################
#################################################
"""
# Externals librairies
try:
    from time import *
    from threading import Thread
    from socket import *
except ModuleNotFoundError:
    try:
        import classes.errors.errors as errors
    except:
        raise RuntimeError("FATAL ERROR. PLEASE REINSTALL THIS REPO OR SET A NEW ISSUE ON GITHUB !")
    raise errors.DependenciesError("""You have to have this librairies installed on your computer :
--> time
--> threading
--> socket
--> and more""")
# Internals files
from classes.filing.save_game import Save as Saver
from classes.filing.open_game import Open as Opener

class MinecraftServer(object):
    """Class of the Minecraft server"""
    def __init__(self, addr=""):
        """Constructor
        Arg:
        - addr : the address (default is localhost)"""
        import time
        self.log("_____________________________________")
        self.log("Starting Server class...")
        self.overworld = []
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

    def save(self):
        """Save the world"""
        saver = Saver(file="worlds/overworld.mcpysrv", data=self.overworld)

    def log(self, basemsg):
        """Log a message
        Arguments :
        - msg : the message to log."""
        import time
        t = time.asctime(time.localtime(time.time()))
        PREFIX = "[{0}] [INFO] : ".format(t[-13:-5])
        msg = PREFIX + basemsg
        print(msg)
        import os
        if os.path.exists("logs.log"):
            with open("logs.log", "r") as logfile:
                logs = logfile.read()
            with open("logs.log", "w") as logfile:
                logfile.write(logs + "\n" + msg)
        else:
            with open("logs.log", "w") as logfile:
                logfile.write(msg)

    def log_error(self, basemsg):
        """Log an error
        Arguments :
        - msg : the error to log."""
        import time
        t = time.asctime(time.localtime(time.time()))
        PREFIX = "[{0}] [ERROR] : ".format(t[-13:-5])
        msg = PREFIX + basemsg
        print(msg)
        import os
        if os.path.exists("logs.log"):
            with open("logs.log", "r") as logfile:
                logs = logfile.read()
            with open("logs.log", "w") as logfile:
                logfile.write(logs + "\n" + msg)
        else:
            with open("logs.log", "w") as logfile:
                logfile.write(msg)

    def log_warning(self, basemsg):
        """Log a warning
        Arguments :
        - msg : the warning to log."""
        import time
        t = time.asctime(time.localtime(time.time()))
        PREFIX = "[{0}] [WARN] : ".format(t[-13:-5])
        msg = PREFIX + basemsg
        print(msg)
        import os
        if os.path.exists("logs.log"):
            with open("logs.log", "r") as logfile:
                logs = logfile.read()
            with open("logs.log", "w") as logfile:
                logfile.write(logs + "\n" + msg)
        else:
            with open("logs.log", "w") as logfile:
                logfile.write(msg)
        

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

class MinecraftSocketServerGestionner(object):
    """The gestionner of the sockets of the server"""
    def __init__(self, addr="", port=25565):
        """Constructor"""
        self.addr = addr
        self.port = port
        self.socket = socket(AF_INET, SOCK_STREAM)      #Good args ?

    def bind(self):
        """Bind the server"""
        self.socket.bind((self.addr, self.port))

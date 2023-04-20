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
        self.worlds = []
        self.addr = (addr, 25565)   #Creating normal socket addr format
        self.socket = MinecraftSocketServerGestionner(addr=self.addr, port=25565)

    def return_worlds(self, filter=None):
        """Return all worlds files find with/without filters
        Arguments:
        - filter (default : None) : can be :
            - "o" : overworld
            - "n" : nether
            - "e" : ender"""
        import os
        if not(os.path.exist("worlds")):
            #If the folder Server/worlds doesn't exists
            self.log_warning("The folder Server/worlds doesn't exist. Returned value : None")
            return None
        elif filter == None:
            #With no filter
            dir = os.listdir("worlds")
            files = []
            for i in dir:
                #For every items in the directory
                if os.path.isfile("worlds/" + i) and i[-8:] == ".mcpysrv":
                    files.append(i)
        elif filter == "o":
            #With filter "overworld" (normal minecraft world)
            dir = os.listdir("worlds")
            files = []
            for i in dir:
                #For every items in the directory
                if os.path.isfile("worlds/" + i) and i[-10:] == "_o.mcpysrv":
                    files.append(i)
        elif filter == "n":
            #With filter "nether" (a world where there isn't any water (too hot))
            dir = os.listdir("worlds")
            files = []
            for i in dir:
                #For every items in the directory
                if os.path.isfile("worlds/" + i) and i[-10:] == "_n.mcpysrv":
                    files.append(i)
        elif filter == "e":
            #With filter "ender" (the world where there is the final Minecraft end boss, the EnderDragon. There is a lot of void.)
            dir = os.listdir("worlds")
            files = []
            for i in dir:
                #For every items in the directory
                if os.path.isfile("worlds/" + i) and i[-10:] == "_e.mcpysrv":
                    files.append(i)
        else:
            #Bad filter
            self.log_error("A bad world filter was set. Impossible to return world. Returned value : None")
            return None
        return files
        

    def start(self):
        """Launch the server"""
        self.load_worlds()

    def load_worlds(self):
        """Load the worlds of the server
        THIS SECTION MUST HAVE CONTRIBUTORS !"""
        
    def create_world(self, name, type="normal"):
        """Create a new world.
        Type can be "normal", "nether" or "end"."""
        

    def open(self):
        """Open the server to clients"""
        self.socket.bind()

    def save(self):
        """Save the world"""
        saver = Saver(file="worlds/overworld.mcpysrv", data=self.overworld)

    def log(self, basemsg):
        """Log a message.
        Argument :
        - basemsg : the message to log."""
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
        """Log an error.
        Argument :
        - basemsg : the error to log."""
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
        """Log a warning.
        Argument :
        - basemsg : the warning to log."""
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

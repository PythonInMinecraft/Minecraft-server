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
    from tkinter import *
    from tkinter.scrolledtext import *
    from tkinter.simpledialog import *
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

    command_list = {}

    def __init__(self, addr=""):
        """Constructor
        Arg:
        - addr : the address (default is localhost)"""
        import time
        print("Please wait...")

        gui_thread = Thread(target=self.launch_gui, name='GUI')
        gui_thread.start()

        sleep(5)
        
        self.log("#{0}".format(time.asctime(time.localtime(time.time()))))
        self.log("_____________________________________")
        self.log("Starting Server class...")
        self.log("_____________________________________")
        #self.addr = (addr, 25565)   #Creating normal socket addr format
        #self.socket = MinecraftSocketServerGestionner(addr=self.addr, port=25565)
        self.log_warning("This version is a developpement version ; launch it will maybe cause some issues.")
        self.worlds = self.return_worlds()
        self.worlds_data = {}       #This dico is : {"world_name":<pythondata>, ...}
        if len(self.worlds) == 0:
            self.log("No worlds found, creating 3 new...")
            self.log_warning("Code not found, skipping...")
            #self.create_world(world_name="world", type="o")
            #self.create_world(world_name="nether", type="n")
            #self.create_world(world_name="end", type="e")
        #self.stop()

    def stop(self):
        """Stop the server."""
        import time
        self.log("Stoping the server...")
        try:
            self.main_gui.destroy()
        except TclError:
            pass
        ...
        exit(0)
    
    def get_cmd(self, target):
        """Get all the commands."""
        if target == "CONSOLE":
            self.command_list = {"/help":"classes.commands.help", "/stop":"classes.commands.stop"}
        else:
            self.command_list = {"/help":"classes.commands.help", "/gamemode":"classes.commands.gamemode", "/stop":"classes.command.stop"}

    def launch_gui(self):
        """Launch the server GUI, with command entry, player list..."""
        self.main_gui = Tk()
        self.main_gui.title("Minecraft server")

        self.main_frame = Frame(self.main_gui)
        self.main_frame.pack()

        self.player_list_frame = Frame(self.main_frame)
        self.player_list_frame.pack(side=LEFT)

        self.log_frame = Frame(self.main_frame)
        self.log_frame.pack(side=LEFT)

        self.command_entry_frame = Frame(self.main_gui)
        self.command_entry_frame.pack()

        #_______________________________

        self.logs_text = ScrolledText(self.log_frame, state="disabled")
        self.logs_text.pack()

        self.player_list = Listbox(self.player_list_frame, width=20, height=24)
        self.player_list.pack()

        self.command_entry = Entry(self.command_entry_frame, width=50)
        self.command_entry.pack(side=LEFT)

        self.command_entry.bind("<Return>", self.get_console_command)

        mainloop()

        """Stop the server when closed"""
        self.stop()

    def get_console_command(self, e=None):
        """Get the command from the gui"""
        cmd = self.command_entry.get()
        self.log("CONSOLE issued server command : {0}".format(cmd))

        self.command_entry.destroy()

        self.command_entry = Entry(self.command_entry_frame, width=50)
        self.command_entry.pack(side=LEFT)

        self.command_entry.bind("<Return>", self.get_console_command)

        self.execute_command(cmd, "CONSOLE")

    def execute_command(self, command, runner):
        """Run a command.
        Arguments :
        - command : the command (str)
        - runner : the player/console/entity who run the command."""
        self.get_cmd(runner)
        if not(len(command) == 0):  #Is the command empty ?
            if command[0] == "/":   #Is it a command ?
                splited = command.split(" ")
                try:
                    path = self.command_list[splited[0]]
                    with open("Server/classes/temp/command_executor.py", "w") as file:
                        file.write("import {0} as cmd".format(path))
                    import classes.temp.command_executor as ce
                    ce.cmd.main(self, runner, splited[1:])
                    del(ce)
                except KeyError:
                    self.log_warning("Unknow command. Type \"/help\" for help.")
            else:
                self.log_warning("This isn't a command !")
                self.send_to_chat(command, runner)  #send to chat

    def send_to_chat(self, msg, entity):
        """Send a message in the chat.
        Arguments:
        - msg : the message (str)
        - entity : who send the message"""
        ...
        

    def return_worlds(self, filter=None):
        """Return all worlds files find with/without filters
        Arguments:
        - filter (default : None) : can be :
            - "o" : overworld
            - "n" : nether
            - "e" : ender"""
        import os
        if filter == None:
            #With no filter
            path = os.getcwd()+"\\Server\\worlds\\"
            dir = os.listdir(path)
            files = []
            for i in dir:
                #For every items in the directory
                if os.path.isfile(path + i) and i[-8:] == ".mcpysrv":
                    files.append(i)
        elif filter == "o":
            #With filter "overworld" (normal minecraft world)
            dir = os.listdir(path)
            files = []
            for i in dir:
                #For every items in the directory
                if os.path.isfile(path + i) and i[-10:] == "_o.mcpysrv":
                    files.append(i)
        elif filter == "n":
            #With filter "nether" (a world where there isn't any water (too hot))
            dir = os.listdir(path)
            files = []
            for i in dir:
                #For every items in the directory
                if os.path.isfile(path + i) and i[-10:] == "_n.mcpysrv":
                    files.append(i)
        elif filter == "e":
            #With filter "ender" (the world where there is the final Minecraft end boss, the EnderDragon. There is a lot of void.)
            dir = os.listdir(path)
            files = []
            for i in dir:
                #For every items in the directory
                if os.path.isfile(path + i) and i[-10:] == "_e.mcpysrv":
                    files.append(i)
        else:
            #Bad filter
            self.log_error("Unknow filter. Impossible to return world. Returned value : None")
            return None
        return files
        

    def start(self):
        """Launch the server"""
        self.load_worlds()

    def load_worlds(self):
        """Load the worlds of the server
        THIS SECTION MUST HAVE CONTRIBUTORS !"""
        
    def create_world(self, world_name, type="o"):
        """Create a new world.
        Arguments:
        - world_name : the name of the world (str)
        - type : can be "o"(overworld), "n"(nether) or "e"(ender). Default : "o"."""
        self.log("Starting creation of the world {0}...")
        if not(type == "o" or type == "n" or type == "e"):      #check type
            l = "The type of the world {0} isn't correct.".format(world_name)
            self.log_error(l)
            self.fatal_error("""Bad world type.
            At:
                - Server/classes/server.py
                    \_ Server().create_world()
                      \_ #check_type section.""")
        name = world_name + "_" + type
        self.worlds.append(name)
        self.generate(name)
        #write the world here.
    
    def generate(self, world):
        """Generate the world.
        BE CAREFUL ! THIS METHOD OVERWRITE EXISTING DATA !
        Argument :
        - world : the world to generate (str)"""
        type = world[-1:]
        self.log("Generating world {0}".format(world))
        self.log_warning("You are overwriting existing data if the world already exists !")
        self.log_warning("Method doesn't be coded.")
        self.fatal_error("""This method doesn't be coded.
        At:
            - Server/classes/server.py
                \_ Server().generate()""")

        
    def fatal_error(self, reason):
        """Raise a fatal error and a crash report.
        Argument :
        - reason : the reason of the crash."""
        self.log_error("FATAL ERROR")
        self.log_error("Reason of the crash :")
        self.log_error(reason)
        self.log_error("If this isn't normal, please send an issue on github. Please check logs for more details.")
        self.log_error("The server is switching off. Closing server : Fatal Error")
        nb = 1
        self.log("Creating crash report file...")
        import os
        while os.path.exists("crash_reports/crash_report_{0}.crash".format(nb)):
            nb += 1
        file = "crash_reports/crash_report_" + str(nb) + ".crash"
        with open(file, "w") as report:
            report.write("""# FATAL ERROR report ({0})
            If this error isn't normal, create an issue on GitHub.
            Reason of the crash :
            {1}
            Post error action : stopping the server (FATAL ERROR)
            This error isn't an enormous error, in this case the server will be stopped without warning and logs.
            --> An antecedent maybe created the error.
            IS THE SERVER MODED ? Maybe not, this version isn't a base-modified version. If you modified the server, 
            The PythoninMinecraft organisation can't do anything.""".format(asctime(localtime(time())), 
                                                                            reason))
            self.log("Succes !")
        self.stop()


    def open(self):
        """Open the server to clients"""
        self.socket.bind()

    def save(self):
        """Save the world"""
        for i in self.return_worlds():
            Saver(file="worlds/overworld.mcpysrv", data=self.worlds[i])

    def log(self, basemsg):
        """Log a message.
        Argument :
        - basemsg : the message to log."""
        import time
        t = time.asctime(time.localtime(time.time()))
        PREFIX = "[{0}] [INFO] : ".format(t[-13:-5])
        msg = PREFIX + basemsg
        print(msg)

        self.logs_text.configure(state="normal")
        self.logs_text.insert(END, msg + "\n")
        self.logs_text.configure(state="disabled")
        self.logs_text.yview(END)

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

        self.logs_text.configure(state="normal")
        self.logs_text.insert(END, msg)
        self.logs_text.configure(state="disabled")
        self.logs_text.yview(END)

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

        self.logs_text.configure(state="normal")
        self.logs_text.insert(END, msg+"\n")
        self.logs_text.configure(state="disabled")
        self.logs_text.yview(END)

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

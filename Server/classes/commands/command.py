"""Command class"""

class CommandExecutor(object):
    #commands:(path, perm, console)
    command_list = {"/help":(0, True), "/gamemode":(2, False), "/stop":(4, True)}
    def onCommand(self, sender:str, command:str, server:object):
        cmd = command.split()
        base_cmd = cmd[0]
        try:
            cmd_perm = self.command_list[base_cmd]
            if base_cmd == "/help":
                if self.help(sender, " ".join(cmd[1:])):
                    server.log("Command executed.")
                else:
                    server.log("An internal error occured while performing this command. Please check the logs for details.")
        except KeyError:
            server.log_error("Unknow command. Please type \"/help\" for help.")

    def perform(self, command, sender, args):
        ...
        

    def help(self, sender:str, arg:str, server:object):
        """On command help"""
        server.log("Help showed to {0} for path {1}.".format(sender, arg))
        if sender == "CONSOLE":
            server.log("""____CONSOLE HELP MENU____""")
            server.log("""- /help <path> --> show the help of the determined path""")
            server.log("""...""")
            return True
        else:
            ...
            return True

    def gamemode(self, target:str, source:str, gamemode:int, server:object):
        if not(target == "CONSOLE"):
            dico_gm = {0:"survival", 1:"creative", 2:"adventure", 3:"spectator"}
            server.log("Changing the gamemode of {0} to {1} by {2}.".format(target, dico_gm[gamemode], source))
            ...
            return True
        else:
            server.log_warning("Impossible to change the gamemode of the console, it is not a player.")
            return False
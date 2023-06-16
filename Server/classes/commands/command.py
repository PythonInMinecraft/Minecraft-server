"""Command class"""

class CommandExecutor(object):
    #commands:(path, perm, console)
    command_list = {"/help":("classes.commands.help", 0, True), 
                    "/gamemode":("classes.commands.gamemode", 2, False), 
                    "/stop":("classes.command.stop", 4, True)}
    def onCommand(self, sender:str, command:str):
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
"""Command class"""

class CommandExecutor(object):
    def onCommand(self, sender:str, command:str):
        ...
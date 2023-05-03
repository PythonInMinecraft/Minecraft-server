def main(server, target, path):
        """Show the help to the specific target"""
        server.log("Help showed to {0} for path {1}.".format(target, path))
        if target == "CONSOLE":
            server.log("""____CONSOLE HELP MENU____""")
            server.log("""- /help <path> --> show the help of the determined path""")
            server.log("""...""")
        else:
            ...
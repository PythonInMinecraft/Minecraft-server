def main(server, target, *args):
        server.log("Help showed to {0} for path {1}.".format(target, " ".join(*args)))
        if target == "CONSOLE":
            server.log("""____CONSOLE HELP MENU____""")
            server.log("""- /help <path> --> show the help of the determined path""")
            server.log("""...""")
        else:
            ...
def main(server, target, *args):
    server.log("Changing the gamemode of {0} to {1} by {2}.".format(*args[0], *args[1], target))

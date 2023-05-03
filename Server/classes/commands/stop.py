def main(server, target, *args):
        server.log("Stopping the server with the command runned by {0}".format(target))
        server.stop()
"""Open a world"""

class Open(object):
    """Open a world. File extention should be .mcpysrv"""
    BLOCKS = {0:"minecraft:air", 1:"minecraft:grass_block", 2:"minecraft:dirt", 3:"minecraft:stone", 4:"minecraft:cobble_stone"}

    def __init__(self, file):
        """Open a world"""
        file = file
        with open(file, "r") as file:
            self.data = file.read()
            return self.decode()
        
    def read(self):
        """read and  decode the world file's data"""
        curent_value = ""
        self.state = 0       #self.state=0 : reading chunk id ; self.state=1 : reading chunk blocks
        for l, item in enumerate(self.data):
            #for every characters in self.data (the file)
            if item == ";":
                self.next()
            elif item == "{":
                if self.state == 0:
                    self.state = 1
                    ...
                else:
                    raise LookupError("An error occured while decoding the file {0} : chunk opened in an other chunk (char {1}).".format(self.file, l))
            elif item == "}":
                if self.state == 1:
                    self.state = 0
                    ...
                else:
                    raise LookupError("An error occured while decoding the file {0} : trying to stop reading chunk without be in a chunk (char {1}).".format(self.file, l))
            elif item == "...":
                raise LookupError("'...' is used in the example for skip all the blocks, or it will be a lot, but it  isn't a valid character. Last think : please don't modify worlds file.")
            else:
                curent_value += item
                continue
            
    def next(self):
        """Go to the next value and apply"""
        ...

    def return_data(self):
        """Return the data rode."""
        ...

if __name__ == "__main__":
    exit(0)
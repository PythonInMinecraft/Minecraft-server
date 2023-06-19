"""Open a world"""

import os

class Open(object):
    """Open a world. File extention should be .mcpysrv"""
    BLOCKS = {0:"minecraft:air", 1:"minecraft:grass_block", 2:"minecraft:dirt", 3:"minecraft:stone", 4:"minecraft:cobble_stone"}

    def __init__(self, file):
        """Open a world"""
        self.file = file
        self.decoded = None
        with open(file, "r") as file:
            self.data = file.read()
        
    def read(self):
        """read and  decode the world file's data"""
        os.chdir(os.getcwd + "\\Server\\worlds")
        self.curent_value = ""
        self.final = []
        self.chunk_actu = ()
        self.chunk_dic = {}
        self.chunk_blocs = []
        self.coord_state = "x"
        self.state = 0       #self.state=0 : reading chunk id ; self.state=1 : reading chunk blocks
        for self.char, item in enumerate(self.data):
            #for every characters in self.data (the file)
            if item == ";":
                self.next()

            elif item == "{":
                if self.state == 0:
                    self.state = 1
                    self.next()
                    self.chunk_actu.append(self.chunk_dic)
                else:
                    raise LookupError("An error occured while decoding the file {0} : chunk opened in an other chunk (char {1}).".format(self.file, self.char))
                
            elif item == "}":
                if self.state == 1:
                    self.state = 0
                    self.next()
                    self.chunk_actu.append(self.chunk_blocs)
                    self.final.append(self.chunk_actu)
                    self.chunk_actu = ()
                else:
                    raise LookupError("An error occured while decoding the file {0} : trying to stop reading chunk without be in a chunk (char {1}).".format(self.file, self.char))
                
            elif item == "...":
                raise LookupError("'...' is used in the example for skip all the blocks, or it will be a lot, but it  isn't a valid character. Last think : please don't modify worlds file.")
            
            else:
                self.curent_value += item
                continue
        
        return self.final
            
    def next(self):
        """Go to the next value and apply"""
        if self.state == 0:
            if self.coord_state == "x":
                self.chunk_dic["x"] = self.curent_value
                self.coord_state = "y"
            elif self.coord_state == "y":
                self.chunk_dic["y"] = self.curent_value
                self.coord_state = "z"
            elif self.coord_state == "z":
                self.chunk_dic["z"] = self.curent_value
                self.coord_state = "x"
            else:
                raise LookupError("Error while decoding chunk id. Please don't touch to the world files.")
            self.curent_value = ""
        elif self.state == 1:
            self.chunk_blocs.append(self.curent_value)
            self.curent_value = ""
        else:
            raise LookupError("An error occured while opening the world : bad state {0}".format(self.state))

    def return_data(self):
        """Return the data rode."""
        return self.final

if __name__ == "__main__":
    exit(0)
"""Save a world"""

class Save(object):
    """Save a world. File extention should be .mcpysrv."""
    BLOCKS = {"minecraft:air":0, "minecraft:grass_block":1, "minecraft:dirt":2, "minecraft:stone":3, "minecraft:cobble_stone":4}

    def __init__(self, file:str, data:list):
        """Save a world"""
        self.data = data
        self.file = file

    def write(self):
        """Write the data"""
        with open(self.file, "w") as file:
            file.write(self.encode(self.data))

    def encode(self, data:list):
        """Encode datas chunks / chuncks"""
        final = ""
        for chunk in data:
            #Save a chunk (16/16/16 blocks)
            coord_chunk = chunk[0]        #C is a dictionnary : c is like this : {"x":00, "y":00, "z":00}
            final += "{0};{1};{2}".format(coord_chunk["x"], coord_chunk["y"], coord_chunk["z"]) + "{"
            for block in chunk[1]:
                #Save a block
                final += str(self.BLOCKS[block])
                final += ";"
            final = final[:-1]
            final += "};"
        return final
    
if __name__ == "__main__":
    exit(0)
"""Save the game"""

class Save(object):
    """Save the game"""
    BLOCKS = {"minecraft:air":0, "minecraft:grass_block":1, "minecraft:dirt":2, "minecraft:stone":3, "minecraft:cobble_stone":4}

    def __init__(self, file, data):
        """Save the game"""
        with open(file, "w") as file:
            file.write(self.encode(data))

    def encode(self, data):
        """Encode datas chunks / chuncks"""
        final = ""
        for chunk in self.data:
            #Save a chunk (16/16/16 blocks)
            c = chunk[0]        #C is a dictionnary : c is like this : {"x":00, "y":00, "z":00}
            final += "{0};{1};{2}{".format(c["x"], c["y"], c["z"])
            for block in chunk[1]:
                #Save a block
                final += self.BLOCKS[block]
                final += ";"
            final = final[:-1]
            final += "};"
        return final
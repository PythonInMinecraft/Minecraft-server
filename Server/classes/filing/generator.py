"""The Generator class"""

class Generator(object):
    def void_generator(self, type="o"):
        """Return a void world"""
        if type == "o":
            mat = "minecraft:stone"
        elif type == "n":
            mat = "minecraft:cobble_stone"
        elif type == "e":
            mat = "minecraft:dirt"
        else:
            mat = "minecraft:stone"
        chunk = []
        for i in range(16*16*16):
            #Repeat for every blocs of the chunk
            chunk.append(mat)
        return [({"x":0, "y":0, "z":0}, chunk)]
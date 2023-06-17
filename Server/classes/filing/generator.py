"""The Generator class"""

class Generator(object):
    def void_generator(self):
        """Return a void world"""
        chunk = []
        for i in range(16*16*16):
            #Repeat for every blocs of the chunk
            chunk.append(3)
        return [({"x":0, "y":0, "z":0}, chunk)]
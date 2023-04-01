"""Save the game"""

class Save(object):
    """Save the game"""
    def __init__(self, file, data):
        """Save the game"""
        with open(file, "w") as file:
            file.write(self.encode(data))

    def encode(self, data):
        """Encode datas chunks / chuncks"""
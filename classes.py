class Room:
    def __init__(self):
        self.exits = {
            "north" : None,
            "south" : None,
            "east" : None,
            "west" : None
            }

        self.key = {
            "north" : None,
            "south" : None,
            "east" : None,
            "west" : None
            }

        self.description = None

        self.items = []

    def Has_Exit(self, direction):
        if self.exits[direction] != None:
            return True
        else:
            return False

class Item:
    def __init__(self):
        self.id = None
        self.name = None
        self.description = None

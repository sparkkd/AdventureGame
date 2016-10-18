class Room:
    def __init__(self):
        self.exits = {
            "north" : None,
            "south" : None,
            "east" : None,
            "west" : None,
            "up" : None,
            "down" : None
            }

        self.locked = {
            "north" : False,
            "south" : False,
            "east" : False,
            "west" : False,
            "up" : False,
            "down" : False
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
        self.name = None

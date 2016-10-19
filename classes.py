class Room:
    
    #The constructor which Initializes all objects for Class Room.
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
        
    #This function checks the current room and the passed direction if it has a valid exit or not.
    def Has_Exit(self, direction):
        if self.exits[direction] != None:
            return True
        else:
            return False

class Item:
    
    #The constructor which Initializes all objects for Class Item.
    def __init__(self):
        self.name = None
        self.id = None
        self.description = None

        self.room_used_in = None
        self.used_text = None

    def Use_Item(self):
        raise NotImplementedError

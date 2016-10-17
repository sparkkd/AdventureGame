class Room:
    def __init__(self):
        self.exits = {
            "North" : None,
            "South" : None,
            "East" : None,
            "West" : None
            }

        self.description = None

        self.items = []

class Item:
    def __init__(self):
        self.name = None

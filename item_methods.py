import player
from map import rooms

def Use_ID(self):
    if player.current_room == rooms["Reception"]:
        rooms["Reception"].key["east"] = None
    else:
        print("no")

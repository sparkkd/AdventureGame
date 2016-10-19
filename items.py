import types

from classes import Item
from item_methods import *
import player

# location : player, opens labs

class Item_ID(Item):
    def __init__(self):
        Item.__init__(self)

        self.id = "id"
        self.name = "id"
        self.description = "Your ID is one of the few things that you've already got on you. Let's hope it comes in handy!"

        self.room_used_in = "reception"
        self.used_text = "You swipe your ID. The computer labs is now open."

    def Use_Item(self, current_room = None, inventory = None):
        if current_room.name.lower() == self.room_used_in and current_room.locked["east"] != False:
            print(self.used_text)
            current_room.locked["east"] = False
        else:
            print("You try bending your ID. Probably not a good idea.")

# location : player, shows a map of the university

class Item_Handbook(Item):
    def __init__(self):
        Item.__init__(self)

        self.id = "handbook"
        self.name = "handbook"
        self.description = "This student handbook has maps for all over the university."

        self.used_text = ""

    def Use_Item(self, current_room = None, inventory = None):
        print("You flip through the handbook. Yep, you already knew all of this.")


# location : N4.07, gained when projector fixed. opens safe.

class Item_Reception_Safe_Keys(Item):
    def __init__(self):
        Item.__init__(self)

        self.id = "code"
        self.name = "a code"
        self.description = "A series of numbers. Surely this is used for something?"

        self.used_text = "You input the code in to the reception safe. You gain a set of keys."
        self.room_used_in = "reception"

    def Use_Item(self, current_room = None, inventory = None):
        has_safe_location = False

        for item in inventory:
            if item.id == "memo with the reception safe location":
                has_safe_location = True
                safe_item = item
            
        if current_room.name.lower() == self.room_used_in and has_safe_location:
            print(self.used_text)
            inventory.remove(self)
            inventory.remove(safe_item)
            inventory.append(Item_Exit_Keys())
        else:
            print("It's a piece of paper with numbers on it. How is this meant to be used here?")


# location : labs, fixes projector

class Item_Projector_Bulb(Item):
    def __init__(self):
        Item.__init__(self)

        self.id = "projector bulb"
        self.name = "a projector bulb"
        self.description = "This doesn't seem like a normal light bulb..."

        self.used_text = "You change the projector bulb and a code displays on the screen. You write it down."
        self.room_used_in = "room n4.07"

    def Use_Item(self, current_room = None, inventory = None):
        if current_room.name.lower() == self.room_used_in:
            print(self.used_text)
            inventory.remove(self)
            inventory.append(Item_Reception_Safe_Keys())
            current_room.description = "The projector bulb fits! The projector produced a concentrated light that hits the large screen. On the screen, in the bottom right corner you notice a 5 digit code reading 81889."
        else:
            print("No, you cannot light up the bulb with sheer willpower. Nice try, though.")

# location : admin, opens reception

class Item_Blank_Keycard(Item):
    def __init__(self):
        Item.__init__(self)

        self.id = "blank keycard"
        self.name = "a blank keycard"
        self.description = "This keycard must open one of the surrounding rooms."

        self.used_text = "You use the keycard. The door to reception is now open!"
        self.room_used_in = "the staircase on floor 1"

    def Use_Item(self, current_room = None, inventory = None):
        if current_room.name.lower() == self.room_used_in and current_room.locked["east"] != False:
            print(self.used_text)
            current_room.locked["east"] = False
        else:
            print("You stare deep in to the plain, white, boring keycard. Its blandness stares right back.")


# location : reception, opens trevithick lecture room

class Item_Trevithick_Keys(Item):
    def __init__(self):
        Item.__init__(self)

        self.id = "trevithick keys"
        self.name = "trevithick keys"
        self.description = "There could be something of use in Trevithick."

        self.used_text = "You open the Trevithick lecture theatre. Sweet!"
        self.room_used_in = "reception"

    def Use_Item(self, current_room = None, inventory = None):
        if current_room.name.lower() == self.room_used_in and current_room.locked["north"] != False:
            print(self.used_text)
            current_room.locked["north"] = False
        else:
            print("You jingle the keys. It's oddly satisfying.")


# location : reception, opens main entrance

class Item_Exit_Keys(Item):
    def __init__(self):
        Item.__init__(self)

        self.id = "exit keys"
        self.name = "exit keys"
        self.description = "Finally, the keys for the exit."

        self.used_text = "You unlock the entrance door."
        self.room_used_in = "the main entrance"

    def Use_Item(self, current_room = None, inventory = None):
        if current_room.name.lower() == self.room_used_in and current_room.locked["north"] != False:
            print(self.used_text)
            current_room.locked["north"] = False
            current_room.description = "The key fits! With a swift turn to the left the door finnaly budges and you feel the cold as the wind blows in form outside."
        else:
            print("Jingle jingle. You hear that? That's the sound of freedom.")


# location : trevithick, shows location of reception keys

class Item_Laptop(Item):
    def __init__(self):
        Item.__init__(self)

        self.id = "laptop"
        self.name = "a laptop"
        self.description = "There's something flashing on the screen."

        self.used_text = "You look at the laptop. It shows the location of a hidden safe in reception. Not very secure, is it?"

    def Use_Item(self, current_room = None, inventory = None):
        if Item_Reception_Safe_Location not in inventory:
            print(self.used_text)
            inventory.append(Item_Reception_Safe_Location())
        else:
            print("You wonder if there are any decent games installed but alas, the battery is dead.")


# location : janitor's shed, opens outside gates

class Item_Cutters(Item):
    def __init__(self):
        Item.__init__(self)

        self.id = "bolt cutters"
        self.name = "bolt cutters"
        self.description = "There's no key in site to unlock the gate. These will have to do."

        self.used_text = "You cut the lock off the gate. Freedom!"
        self.room_used_in = "outside the entrance"
        self.used = False

    def Use_Item(self, current_room = None, inventory = None):
        if current_room.name.lower() == self.room_used_in:
            print(self.used_text)
            inventory.append(Item_Reception_Safe_Location())
            self.used = True
            current_room.description = "The bolt cutters easily break the chain around the gate. The gate is now open!!"
        else:
            print("Clip clip. Clip clip.")

# added when laptop is used

class Item_Reception_Safe_Location(Item):
    def __init__(self):
        Item.__init__(self)

        self.id = "memo with the reception safe location"
        self.name = "a memo with the reception safe location"
        self.description = "A crude drawing showing the location of the reception's safe."

    def Use_Item(self, current_room = None, inventory = None):
        print("You admire your artistry. On second thoughts, it's not that impressive.")

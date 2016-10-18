from classes import Item
from map import rooms
from item_methods import *

item_id = Item()
item_id.id = "id"
item_id.name = "id"
item_id.description = "Your ID is one of the few things that you've already got on you. Let's hope it comes in handy!"
item_id.room_used_in = rooms["Reception"]
item_id.used_text = "You swipe your ID. The computer labs is now open."
item_id.Use_Item = Use_ID()

item_handbook = Item()
item_handbook.id = "handbook"
item_handbook.name = "handbook"
item_handbook.description = "This student handbook has maps for all over the university."

item_reception_keys = Item()
item_reception_keys.id = "reception keys"
item_reception_keys.name = "reception keys"
item_reception_keys.description = "These keys must be for the reception."

# location : labs

item_projector_bulb = Item()
item_projector_bulb.id = "projector_bulb"
item_projector_bulb.name = "projector_bulb"
item_projector_bulb.description = "This doesn't seem like a normal light bulb..."

# location : admin, opens reception

item_blank_keycard = Item()
item_blank_keycard.id = "blank keycard"
item_blank_keycard.name = "a blank keycard"
item_blank_keycard.description = "This key must open one of the surrounding rooms."

# location : reception

item_trevithick_keys = Item()
item_trevithick_keys.id = "trevithick keys"
item_trevithick_keys.name = "trevithick keys"
item_trevithick_keys.description = "There could be something of use in Trevithick."

# location : reception

item_exit_keys = Item()
item_exit_keys.id = "exit keys"
item_exit_keys.name = "exit keys"
item_exit_keys.description = "Finally, the keys for the exit."

# location : trevithick

item_laptop = Item()
item_laptop.id = "laptop"
item_laptop.name = "laptop"
item_laptop.description = "There's something flashing on the screen."

# location : janitor's shed

item_trevithick_keys = Item()
item_trevithick_keys.id = "bolt cutters"
item_trevithick_keys.name = "bolt cutters"
item_trevithick_keys.description = "There's no key in site to unlock the gate. These will have to do."

import types

from classes import Item
import item_methods

# location : player, opens labs
item_id = Item()
item_id.id = "id"
item_id.name = "id"
item_id.description = "Your ID is one of the few things that you've already got on you. Let's hope it comes in handy!"
item_id.room_used_in = "Labs"
item_id.used_text = "You swipe your ID. The computer labs is now open."
item_id.Use_Item = types.MethodType(Use_ID, item_id)

# location : player, shows a map of the university
item_handbook = Item()
item_handbook.id = "handbook"
item_handbook.name = "handbook"
item_handbook.description = "This student handbook has maps for all over the university."


# location : N4.07, opens safe in reception
item_reception_keys = Item()
item_reception_keys.id = "reception keys"
item_reception_keys.name = "reception keys"
item_reception_keys.description = "These keys must be for the reception."
item_reception_keys.room_used_in = "Reception"
item_reception_keys.used_text = ""


# location : labs, fixes projector
item_projector_bulb = Item()
item_projector_bulb.id = "projector_bulb"
item_projector_bulb.name = "projector_bulb"
item_projector_bulb.description = "This doesn't seem like a normal light bulb..."
item_projector_bulb.room_used_in = "N4.07"
item_projector_bulb.used_text = ""


# location : admin, opens reception
item_blank_keycard = Item()
item_blank_keycard.id = "blank keycard"
item_blank_keycard.name = "a blank keycard"
item_blank_keycard.description = "This keycard must open one of the surrounding rooms."
item_blank_keycard.room_used_in = "Reception"
item_blank_keycard.used_text = ""


# location : reception, opens trevithick lecture room
item_trevithick_keys = Item()
item_trevithick_keys.id = "trevithick keys"
item_trevithick_keys.name = "trevithick keys"
item_trevithick_keys.description = "There could be something of use in Trevithick."
item_trevithick_keys.room_used_in = "Trevithick"
item_trevithick_keys.used_text = ""


# location : reception, opens main entrance
item_exit_keys = Item()
item_exit_keys.id = "exit keys"
item_exit_keys.name = "exit keys"
item_exit_keys.description = "Finally, the keys for the exit."
item_exit_keys.room_used_in = "Entrance"
item_exit_keys.used_text = ""


# location : trevithick, shows location of reception keys
item_laptop = Item()
item_laptop.id = "laptop"
item_laptop.name = "laptop"
item_laptop.description = "There's something flashing on the screen."
item_laptop.room_used_in = "Trevithick"
item_laptop.used_text = ""


# location : janitor's shed, opens outside gates
item_cutters = Item()
item_cutters.id = "bolt cutters"
item_cutters.name = "bolt cutters"
item_cutters.description = "There's no key in site to unlock the gate. These will have to do."
item_cutters.room_used_in = "Outside"
item_cutters.used_text = ""
#from items import *
from classes import Room
import items

# Declaring Reception as a Room object. 
room_reception = Room()
<<<<<<< HEAD

# Reception's name, valid exists, locked rooms, description, and items.
room_reception.name = "reception"
=======
room_reception.name = "Reception"
>>>>>>> 937f3b1ea8d01b93a9277f98aa6127741340afdf
room_reception.exits["east"] = "Labs"
room_reception.exits["north"] = "Trevithick"
room_reception.exits["west"] = "Middle staircase"
room_reception.locked["east"] = True
room_reception.locked["north"] = True
room_reception.description = """You are in a long winding corridor wth a large desk infront of you.
Next to you is the main reception. Behind reception is dark. You can't see much apart from files and
records. There must be something in here that is useful."""
room_reception.items = [items.Item_Trevithick_Keys()]

# Declaring Admins as a Room object.
room_admins = Room()
# Admins' name, valid exists, description, and items.
room_admins.name = "Admins room"
room_admins.exits["east"] = "Middle staircase"
room_admins.description = """You come to a small green door with a small circular window near the top. 
Next to the door a sign reads "Admins Room". Inside you can see the admins large
desk. The computer on the desk seems to be on as a small green light illuminates the
smooth wooden surface. In the top draw of the desk there's a blank keycard. What could this be for?"""
room_admins.items = [items.Item_Blank_Keycard()]

# Declaring trevithick as a Room object. 
room_trevithick = Room()

# trevithick' name, valid exists, description, and items.
room_trevithick.name = "the Trevithick lecture room"
room_trevithick.exits["south"] = "Reception"
room_trevithick.description = """Inside the trevithick theatre is just how you remember it.
you notice there is a small laptop at the back of the room on one of the desks.
Why is that here?"""
room_trevithick.items = [items.Item_Laptop()]

# Declaring trevithick as a Room object.
room_labs = Room()

# Labs' name, valid exists, description, and items.
room_labs.name = "the computer labs"
room_labs.exits["west"] = "Reception"
room_labs.description = """The labs are quiet and dark. You can see the computers and chairs all sitting still
as the wind whistles outside. One of the pannels in the room has been left standing upright
in the middle of the room, and a small backpack resides on the window sill. You also notice a small box with a
bulb on top of it"""
room_labs.items = [items.Item_Projector_Bulb()]

# Declaring N407 as a Room object.
room_n407 = Room()

# N407 name, valid exists, and description.
room_n407.name = "Room N4.07"
room_n407.exits["west"] = "Top staircase"
room_n407.description = """In the large lecture theatre, there is just enough light to see around. The projector
controls lie on the desk at the front. The computer is turned off and pieces of paper are 
still sprawled over the desk. Near the back road is a red backpack, which has been left on 
one of the chairs."""

# Declaring janitor as a Room object.
room_janitor = Room()

#Janitor name, valid exists, description, and items.
room_janitor.name = "the janitor's room"
room_janitor.exits["east"] = "Outside"
room_janitor.description = """The janitor's shed is old and dirty. You manage to squeeze in through the small rusted
door. You see many different tools and materials, but your eye is caught by a pair of large iron bolt cutters. These
might be useful."""
room_janitor.items = [items.Item_Cutters()]

# Declaring outside as a Room object.
room_outside = Room()

#outside name, valid exists, and description.
room_outside.name = "outside the entrance"
room_outside.exits["west"] = "Janitor"
room_outside.exits["south"] = "Entrance"
room_outside.description = """The outside is illuminated by the street lights in the street behind the large bolted gates.
After walking around you see the only viable way to exit is through the gates, but a thick 
padlocked chain prevents them from opening."""

# Declaring entrance as a Room object.
room_entrance = Room()

# Reception's name, valid exists, locked rooms, and description.
room_entrance.name = "the main entrance"
room_entrance.exits["north"] = "Outside"
room_entrance.exits["west"] = "Ground staircase"
room_entrance.locked["north"] = True
room_entrance.description = """The main entrance is a large room slightly illuminated by the small amount of light outside.
You cannot open the large glass doors."""

# Declaring top staircase as a Room object.
room_staircase_top = Room()

# Top staircase name, valid exists, and description.
room_staircase_top.name = "the staircase on Floor 2"
room_staircase_top.exits["east"] = "N4.07"
room_staircase_top.exits["down"] = "Middle staircase"
room_staircase_top.description = """The top floor, the staircase only leads down."""

# Declaring middle staircase as a Room object.
room_staircase_middle = Room()

# Middle staircase name, valid exists, locked rooms, and description.
room_staircase_middle.name = "the staircase on Floor 1"
room_staircase_middle.exits["east"] = "Reception"
room_staircase_middle.exits["west"] = "Admins"
room_staircase_middle.exits["up"] = "Top staircase"
room_staircase_middle.exits["down"] = "Ground staircase"
room_staircase_middle.locked["east"] = True
room_staircase_middle.description = """The first floor, the staircase leads up and down."""

# Declaring ground staircase as a Room object.
room_staircase_ground = Room()

# Ground staircase name, valid exists, and description.
room_staircase_ground.name = "the staircase on Floor 0"
room_staircase_ground.exits["east"] = "Entrance"
room_staircase_ground.exits["up"] = "Middle staircase"
room_staircase_ground.description = """The bottom floor, the staircase only leads up."""

rooms = {
    "Reception": room_reception,
    "Admins": room_admins,
    "Trevithick": room_trevithick,
    "Labs": room_labs,
    "N4.07": room_n407,
    "Janitor": room_janitor,
    "Outside": room_outside,
    "Entrance": room_entrance,
    "Top staircase": room_staircase_top,
    "Middle staircase": room_staircase_middle,
    "Ground staircase": room_staircase_ground
}

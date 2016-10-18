#from items import *
from classes import Room
from items import *

room_reception = Room()
room_reception.name = "reception"
room_reception.exits["south"] = "Admins"
room_reception.exits["east"] = "Labs"
room_reception.exits["north"] = "Trevithick"
room_reception.exits["west"] = "Middle staircase"
room_reception.key["east"] = item_id
room_reception.description = """You are in a long winding corridor wth a large desk infront of you.
Next to you is the main reception. behind reception is dark, but you can 
just about make out a small safe in the corner of the room. The door 
leading to behind the desk is locked but you see a small scanner next to 
the handle. Behind you is a dark staircase leading up and down."""
room_reception.items = [item_exit_keys]

room_admins = Room()
room_admins.name = "Admin's room"
room_admins.exits["north"] = "Reception"
room_admins.description = """You come to a small green door with a samll circular window near the top. 
Next to the door a sign reads, Admins Room. Inside you can see the admins large
desk. The computer on the desk seems to be on as small green light illuminate the
smooth wooden surface. The outline of other objects on the desk are barely visable
in the dark, but you can just about make out a large mug on the desk and a large book."""
room_admins.items = [item_blank_keycard]

room_trevithick = Room()
room_trevithick.name = "the Trevithick lecture room"
room_trevithick.exits["south"] = "Reception"
room_trevithick.description = """You approach the large wooden double doors of the T2.09 lecture room. You push on 
the door but it does not budge. The inside is pitch black. A key hole resides on the 
door."""
room_trevithick.items = [item_laptop]

room_labs = Room()
room_labs.name = "the computer labs"
room_labs.exits["west"] = "Reception"
room_labs.description = """The labs are quiet and dark. You can see the computers and chairs all sitting still
as the wind whistles outside. You can see one of the pannels in the room has been left 
standing upright in the middle of the room, and a small backback resides on the window 
sill. The door is locked as usual, but you remember that it is opened by a swift swipe 
of your student ID card on the black censor to the right of the door."""
room_labs.items = [item_projector_bulb]

room_n407 = Room()
room_n407.name = "Room N4.07"
room_n407.exits["west"] = "Top staircase"
room_n407.description = """In the large lecture theatre, there is just enough light to see around. The projector
controls lie on the desk at the front. The computer is turned off and pieces of paper are 
still sprawled over the desk. Near the back road is a red backpack, which has been left on 
one of the chairs."""
room_n407.items = [item_reception_keys]

room_janitor = Room()
room_janitor.name = "the janitor's room"
room_janitor.exits["east"] = "Outside"
room_janitor.description = """The outside is illuminated by the street lights in the steet behind the large bolted gates.
after walking around you see the only viable way to exit is through the gates, but a thick 
padlocked chain prevents them from opening."""
room_janitor.items = [item_trevithick_keys]

room_outside = Room()
room_outside.name = "outside the entrance"
room_outside.exits["west"] = "Janitor"
room_outside.exits["south"] = "Entrance"
room_outside.description = """The janitor's room door is locked shut and won't budge. Through the small fogged up window
you can see only darkness apart from the light switch on the wall and a large mop in the near 
corner."""

room_entrance = Room()
room_entrance.name = "the main entrance"
room_entrance.exits["north"] = "Outside"
room_entrance.exits["west"] = "Ground staircase"
room_entrance.description = """The main entrance is a large room slightly illuminated by the small amount of light outside.
You cannot open the large glass doors."""

room_staircase_top = Room()
room_staircase_top.name = "the staircase on Floor 2"
room_staircase_top.exits["east"] = "N4.07"
room_staircase_top.exits["down"] = "Middle staircase"
room_staircase_top.description = """The top floor, the staircase only leads down."""

room_staircase_middle = Room()
room_staircase_middle.name = "the staircase on Floor 1"
room_staircase_middle.exits["east"] = "Reception"
room_staircase_middle.exits["up"] = "Top staircase"
room_staircase_middle.exits["down"] = "Ground staircase"
room_staircase_middle.description = """The first floor, the staircase leads up and down."""

room_staircase_ground = Room()
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

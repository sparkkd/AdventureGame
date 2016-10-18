#from items import *

room_reception = {
    "name": "Reception",

    "description":
    """You are in a long winding corridor wth a large desk infront of you.
    Next to you is the main reception. behind reception is dark, but you can 
    just about make out a small safe in the corner of the room. The door 
    leading to behind the desk is locked but you see a small scanner next to 
    the handle. Behind you is a dark staircase leading up and down.""",

    "exits": {"south": "Admins", "east": "Tutor", "west": "Parking", "up": "Entrance", "down" : ""},

    "items": []
}

room_admins = {
    "name": "Admin's room",

    "description":
    """You come to a small green door with a samll circular window near the top. 
    Next to the door a sign reads, Admins Room. Inside you can see the admins large
    desk. The computer on the desk seems to be on as small green light illuminate the
    smooth wooden surface. The outline of other objects on the desk are barely visable
    in the dark, but you can just about make out a large mug on the desk and a large book.""",

    "exits":  {"north": "Reception"},

    "items": []
}

room_trevithick = {
    "name": "The Trevithick lecture room",

    "description":
    """You approach the large wooden double doors of the T2.09 lecture room. You push on 
    the door but it does not budge. The inside is pitch black. A key hole resides on the 
    door.""",

    "exits": {"west": "Reception"},

    "items": []
}

room_labs = {
    "name": "The computer labs",

    "description":
    """The labs are quiet and dark. You can see the computers and chairs all sitting still
    as the wind whistles outside. You can see one of the pannels in the room has been left 
    standing upright in the middle of the room, and a small backback resides on the window 
    sill. The door is locked as usual, but you remember that it is opened by a swift swipe 
    of your student ID card on the black censor to the right of the door.""",

    "exits": {"east": "Office", "south": "Reception"},

    "items": []
}

room_n407 = {
    "name": "Room N4.07",

    "description":
    """In the large lecture theatre, there is just enough light to see around. The projector
    controls lie on the desk at the front. The computer is turned off and pieces of paper are 
    still sprawled over the desk. Near the back road is a red backpack, which has been left on 
    one of the chairs.""",

    "exits": {"west": "Parking"},

    "items": []
}

room_janitor = {
   "name": "The janitor's room",

    "description":
    """The janitor's room door is locked shut and won't budge. Through the small fogged up window
    you can see only darkness apart from the light switch on the wall and a large mop in the near 
    corner.""",

    "exits": {"west": "Parking"},

    "items": [] 
}

room_outside = {
    "name": "Outside the entrance",

    "description":
    """The outside is illuminated by the street lights in the steet behind the large bolted gates.
    after walking around you see the only viable way to exit is through the gates, but a thick 
    padlocked chain prevents them from opening.""",

    "exits": {"west": "Parking"},

    "items": []
}

room_entrance = {
    "name": "The main entrance",

    "description":
    """The main entrance is a large room slightly illuminated by the small amount of light outside.
    You cannot open the large glass doors.""",

    "exits": {"west": "Parking"},

    "items": []
}

rooms = {
    "Reception": room_reception,
    "Admins": room_admins,
    "Trevithick": room_trevithick,
    "Labs": room_labs,
    "N4.07": room_n407,
    "Janitor": room_janitor,
    "Outside": room_outside,
    "Entrance": room_entrance
}

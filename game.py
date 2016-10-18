import player, input_parser
from map import rooms

def Game():
    player.current_room = rooms["N4.07"]
    
    finished = False
    
    while not finished:
        Print_Information()
        
        user_input = Process_Command(input_parser.Parse_Input(input("""
What do you do?

>>> """)))

def Print_Information():
    # print room description
    Print_Room_Description()

    Print_Room_Exits()

    Print_Room_Items()

    Print_Inventory_Items()

def Print_Room_Description():
    print("""%s

%s
"""%(player.current_room.name.upper(), player.current_room.description))

def Print_Room_Exits():
    for ex in player.current_room.exits:
        if player.current_room.exits[ex] != None:
            if ex == "up" or ex == "down":
                print("%s is %s."%(ex.upper(), rooms[player.current_room.exits[ex]].name))
            else:
                print("To the %s is %s."%(ex.upper(), rooms[player.current_room.exits[ex]].name))

def Print_Room_Items():
    item_names = []

    for item in player.current_room.items:
        item_names.append(item.name)

    if item_names != []:
        print("There is %s."%(Join_Items(item_names)))

def Print_Inventory_Items():
    item_names = []

    for item in player.inventory:
        item_names.append(item.name)

    if item_names != []:
        print("You have %s."%(Join_Items(item_names)))

def Join_Items(array):
    return ", ".join(array)

def Process_Command(user_input):
    # call correct function
    
    if user_input[0] in ["go", "move"]:
        Execute_Go(user_input)
    elif user_input[0] in ["drop"]:
        Execute_Drop(user_input)
    elif user_input[0] in ["take"]:
        Execute_Take(user_input)
    elif user_input[0] in ["use"]:
        Execute_Use(user_input)
    else:
        print("You can't do that!")

def Execute_Go(user_input):
    if len(user_input) <= 1:
        print("Go where?")
    else:
        if player.current_room.Has_Exit(user_input[1]):
            if not player.current_room.key[user_input[1]] != None:
                player.current_room = rooms[player.current_room.exits[user_input[1]]]
            else:
                print("You try the door, but it's locked.")
        else:
            print("You cannot go there!")

def Execute_Drop(user_input):
    if len(user_input) <= 1:
        print("Drop what?")
    else:
        user_input = " ".join(user_input[1:])
        
        found = False
        
        for item in player.inventory:
            if item.id == user_input:
                found = True

                player.current_room.items.append(item)
                player.inventory.remove(item)

        if not found:
            print("You can't drop that!")

def Execute_Take(user_input):
    if len(user_input) <= 1:
        print("Take what?")
    else:
        user_input = " ".join(user_input[1:])
        
        found = False
        
        for item in player.current_room.items:
            
            if item.id == user_input:
                found = True

                player.inventory.append(item)
                player.current_room.items.remove(item)

        if not found:
            print("You can't take that!")

def Execute_Use(user_input):
    if len(user_input) <= 1:
        print("Use what?")
    else:
        user_input = " ".join(user_input[1:])

        found = False

        for item in player.inventory:
            if item.id == user_input:
                found = True

                item.Use_Item()

        if not found:
            print("You can't use that.")

if __name__ == "__main__":
    Game()

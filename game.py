import player, input_parser
import map, janitor
from time import sleep
from sys import exit

#Var initiation for janitor
janitorActive = False

#Attempt to make the console not look so cluttered
def ClearConsole():
    sleep(0.75)
    print()
    for i in range(0, 4):
        print("...")
        sleep(0.2)
    print()

GameOver = """   _____                         ____                
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   """

#A function to stop the game closing instantly without the user knowing
def EndGame():
    ClearConsole()
    print(GameOver)
    sleep(5)
    exit()
                                                                                                    
#Start of the game
def Game():
    player.current_room = map.rooms["N4.07"]
    
    finished = False
    
    while not finished:        
        if janitorActive == False:
            Print_Information()
        
        user_input = Process_Command(input_parser.Parse_Input(input("""
What do you do?

>>> """)))

        print()

#finishes game
        for item in player.inventory:
            if item.name == "bolt cutters":
                if item.used:
                    finished = True
                    EndGame()
                    
# print room description
def Print_Information():
    Print_Room_Description()

    Print_Room_Exits()

    Print_Room_Items()

    Print_Inventory_Items()

#prints the room name and description
def Print_Room_Description():
    print("""%s

%s
"""%(player.current_room.name.upper(), player.current_room.description))

#prints the avaliable exits from each room
def Print_Room_Exits():
    for ex in player.current_room.exits:
        if player.current_room.exits[ex] != None:
            if ex == "up" or ex == "down":
                print("%s is %s."%(ex.upper(), map.rooms[player.current_room.exits[ex]].name))
            else:
                print("To the %s is %s."%(ex.upper(), map.rooms[player.current_room.exits[ex]].name))

#prints the items that are in the room
def Print_Room_Items():
    item_names = []

    for item in player.current_room.items:
        item_names.append(item.name)

    if item_names != []:
        print("\nThere is %s."%(Join_Items(item_names)))

#prints items that are in the players inventory
def Print_Inventory_Items():
    item_names = []

    for item in player.inventory:
        item_names.append(item.name)

    if item_names != []:
        print("\nYou have %s."%(Join_Items(item_names)))

#makes a list of items in the players inventory to print
def Join_Items(array):
    return ", ".join(array)

def Process_Command(user_input):
    # call correct function
    global janitorActive
    if not janitorActive:
        if user_input[0] in ["go", "move"]:
            Execute_Go(user_input)
        elif user_input[0] in ["drop"]:
            Execute_Drop(user_input)
        elif user_input[0] in ["take"]:
            Execute_Take(user_input)
        elif user_input[0] in ["use"]:
            Execute_Use(user_input)
        elif user_input[0] in ["look"]:
            Execute_Look(user_input)
        else:
            print("\nYou can't do that!")
    else: #New
        if user_input[0] in ["use"]:
            if user_input[1] in ["cookie"]:
                print("You give the janitor your cookie\n")
                print("'"+"Alright... I'll let you off this time, but you get out of here as soon as possible. I don't want to see you again!"+"'")
                for item in player.inventory:
                    if item.id == "cookie":
                        player.inventory.remove(item)
                        break
                janitorActive = False
            else:
                print("\nHe doesn't want that item...")
        else:
            print("The janitor is still waiting and won't let you go without an answer!")    

    ClearConsole()

#allows the player to go from room to room
def Execute_Go(user_input):
    global janitorActive
    if len(user_input)>1:
        if user_input[1] in map.directions:
            if player.current_room.Has_Exit(user_input[1]):
                if not player.current_room.locked[user_input[1]]:
                    player.current_room = map.rooms[player.current_room.exits[user_input[1]]]
                    if not janitor.janitorSeen:
                        if janitor.JanitorCanAppear():
                            janitor.CallJanitor()
                            HasCookie = False
                            for item in player.inventory:
                                if item.id == "cookie":
                                    HasCookie = True
                                    break 
                            if not HasCookie: 
                                print("'"+"Nothing!? Well I guess you're coming with me!"+"'")
                                EndGame() 
                            Print_Inventory_Items()
                            janitorActive = True
                        if player.current_room == map.cookieRoom:
                            janitor.CookieSeen()                       			
                else:
                    print("\nYou try the door, but it's locked.")
            else:
                print("\nYou cannot go there!")
        else:
            print("\nGo where?")
    else: #Sometimes I hate nesting.
        print("\nGo where?")

#Allows the player to drop items
def Execute_Drop(user_input):
    if len(user_input) <= 1:
        print("\nDrop what?")
    else:
        user_input = " ".join(user_input[1:])
        
        found = False
        
        for item in player.inventory:
            if item.id == user_input:
                found = True

                player.current_room.items.append(item)
                player.inventory.remove(item)

        if not found:
            print("\nYou can't drop that!")

#Allows the player to take items
def Execute_Take(user_input):
    if len(user_input) <= 1:
        print("\nTake what?")
    else:
        user_input = " ".join(user_input[1:])
        
        found = False
        
        for item in player.current_room.items:
            
            if item.id == user_input:
                found = True
                if len(player.inventory) < 4:
                        player.inventory.append(item)
                        player.current_room.items.remove(item)
                elif len(player.inventory) >= 4:
                        print("Your inventory is full.")

        if not found:
            print("\nYou can't take that!")

#allows the player to use items to unlock doors
def Execute_Use(user_input):
    if len(user_input) <= 1:
        print("\nUse what?")
    else:
        user_input = " ".join(user_input[1:])

        found = False

        for item in player.inventory:
            if item.id == user_input:
                found = True

                item.Use_Item(player.current_room, player.inventory)

        if not found:
            print("\nYou can't use that.")

#Allows the player to look at items in the inventory
def Execute_Look(user_input):
    if len(user_input) <= 1:
        print("\nLook at what?")
    else:
        user_input = " ".join(user_input[1:])

        found = False

        for item in player.inventory:
            if item.id == user_input:
                found = True

                print(item.description)

        if not found:
            print("\nYou can't look at that.")
if __name__ == "__main__":
    print("╦ ╦┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ┌┬┐┌─┐")
    print("║║║├┤ │  │  │ ││││├┤    │ │ │")
    print("╚╩╝└─┘┴─┘└─┘└─┘┴ ┴└─┘   ┴ └─┘")
    print("╔═╗┬ ┬┌┬┐┬ ┬┌─┐┌┐┌  ╔═╗┌─┐┌─┐┌─┐┌─┐┬ ┬┌┬┐")
    print("╠═╝└┬┘ │ ├─┤│ ││││  ╠═╝├─┤└─┐└─┐│ ││ │ │ ")
    print("╩   ┴  ┴ ┴ ┴└─┘┘└┘  ╩  ┴ ┴└─┘└─┘└─┘└─┘ ┴ ")
    print()
    ClearConsole()
    Game()

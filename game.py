import player, input_parser, game_map

def Game():
    player.current_room = game_map.start_room
    
    finished = False
    
    while not finished:
        Print_Information()
        
        user_input = Process_Command(input_parser.Parse_Input(input("""What do you do?

>>> """)))

def Print_Information():
    # print room description

    # print room items
    pass

def Process_Command(user_input):
    # process user input using parser module

    # call correct function
    
    if user_input[0] in ["go", "move"]:
        Execute_Go(user_input)
    elif user_input[0] in ["drop"]:
        "drop item"
    elif user_input[0] in ["take"]:
        "take item"
    else:
        print("You can't do that!")

def Execute_Go(user_input):
    if len(user_input) <= 1:
        print("Go where?")
    else:
        if player.current_room.Has_Exit(user_input[1]):
            player.current_room = player.current_room.exits[user_input[1]]
        else:
            print("You cannot go there!")

def Execute_Drop():
    pass

def Execute_Take():
    pass

if __name__ == "__main__":
    Game()

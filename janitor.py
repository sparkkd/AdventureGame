import randomizer

#Var initiation
cookieSeen = False
janitorSeen = False

#Switches our global variable from the game script
def CookieSeen():
    global cookieSeen
    cookieSeen = True 

#Queries if the janitor should be called
def JanitorCanAppear():
    Can = False
    if janitorSeen == False:
        if cookieSeen == True:
            Can = randomizer.Chance()
    return Can

#Provides context for janitors visit
def CallJanitor():
    global janitorSeen
    janitorSeen = True
    print("As you enter, a strange figure emerges from the shadows. It looks like the janitor! "+
    "'"+"What are you doing here!?"+"'"+", he shouts. "+"'"+"You shouldn't be here, i'm taking you "+
    "to Kirill's office."+"'"+" He pauses for a second. "+"'"+"Unless... you have something for me?"+"'"+
    " You notice his stomach rumbling.")

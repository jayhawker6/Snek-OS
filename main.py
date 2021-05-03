### IMPORTS ###
import sys
import time
import random
from os import system, name

### VARS ###
badjokes = [
 "Why is it a bad idea to iron your four-leaf clover? Cause you shouldn't press your luck.",
 "I ordered a chicken and an egg from Amazon. I'll let you know.",
 "I can't take my dog to the pond anymore because the ducks keep attacking him. That's what I get for buying a pure bread dog.",
 "My wife said I was immature. So I told her to get out of my fort.",
 "I didn't want to believe that my dad was stealing from his job as a traffic cop, but when I got home, all the signs were there.",
 "I spent a lot of time, money, and effort childproofing my house… but the kids still get in.",
 "What rock group has four men that don't sing? Mount Rushmore.",
 "How many tickles does it take to make an octopus laugh? It takes ten... ten tickles!",
 "What do sprinters eat before a race? Nothing, they fast!",
 "What happens when you go to the bathroom in France? European.",
 "Why did the invisible man turn down the job offer? He couldn't see himself doing it!",
 "Want to hear a joke about construction? I'm still working on it!",
 'I was really angry at my friend Mark for stealing my dictionary. I told him, "Mark, my words!"',
 "What is the tallest building in the world? The library—it's got the most stories.",
 "Within minutes, the detectives knew what the murder weapon was. It was a brief case.",
 "My wife told me I had to stop acting like a flamingo. So I had to put my foot down!",
 "I don't play soccer because I enjoy the sport. I'm just doing it for kicks!"
 ]
 

### FUNCTIONS ###

## Clear Function from geeksforgeeks ##
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

## Progress bar from from stackoverflow ##
def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

#Login function from yours truly ##
def login():
    input("Hello! Press enter to begin the login sequence!")
    attempts = 3
    while True:
        username = "snek"
        password = "nom nom"
        clear()
        if attempts == 0:
            sys.exit(">|<-> Passwords Incorrect! Come back never! <->|<")
        userinput = input("Username : ")
        passinput = input("Password : ")
        if userinput == username:
            if passinput == password:
                attempts = 3
                break
            else:
                attempts -= 1
                continue
        else:
            attempts -= 1
            continue
    clear()
    input("Nice gamer move! Press enter to continue to your lair!")
    clear()

### CODE ###

## Call progress bar ##
for i in progressbar(range(random.randint(15,24)), "Loading Snek OS", 40):
    time.sleep(random.uniform(.1,.5))

clear()

## Login ##
login()

## Main Menu ##
while True:
    clear()
    try:
        sysput = int(input("""
Welcome to Snek OS! Your options are listed below!

1 - InterWebz
2 - Steam
3 - Dad Joke
4 - Diagnose Computer
5 - Not a virus.exe
6 - Die

9 - Logout

"""))
    except ValueError:
        clear()
        continue
    if sysput == 1: # InterWebz
        clear()
        continue
    elif sysput == 2: # Steam
        while True:
            clear()
            try:
                steamput = int(input("""
Welcome to steam by valve! How may we crash your computer today?
1 - Dos Box
2 - Half Life 3
3 - CS:GO

9 - Back
"""))
            except ValueError:
                continue
            if steamput == 1: # Steam/Dosbox
                clear()
                input("Compatability error! Please downgrade to Snek ME!")
                continue
            elif steamput == 2: # Steam/HL3
                clear()
                input("""
Your pre-order has been accepted! Please proceed to wait 10,000 years until release. Thank you!
""")
                continue
            elif steamput == 3: #Steam/CS:GO
                clear()
                for i in progressbar(range(10), "Connecting to CS:GO", 40):
                    time.sleep(.1)
                input("""
Your account has been closed.

Time: 49.9 years
Reason: Cheating
Moderator: VAC
Time in game: 0.01

If you feel like this is a false ban, please don't bother contacting support. We don't care!
""")
                continue
            elif steamput == 9: #Steam/Back
                break
            else:
                continue
        continue
    elif sysput == 3: #Dad Jokes
        clear()
        input(random.choice(badjokes))
        continue
    elif sysput == 4: #Diagnose
        while True:
            clear()
            try:
                diagput = int(input("""
Welcome to the computer diagnosis tool! Would you like to view your computer's status?
1 - Yes
2 - No

9 - Back
"""))
            except ValueError:
                continue
            if diagput == 1: #Diagnose/yes
                clear()
                input("According to my sources, your computer is ON. You are welcome!")
                break
            elif diagput == 2: #Diagnose/no
                clear()
                input("Why did you come then?")
                break
            elif diagput == 9: #Diagnose/back
                clear()
                break
            else:
                continue
        clear()
        continue
    elif sysput == 5:
        clear()
        continue
    elif sysput == 6:
        clear()
        input("You are now dead. Congradulations! Now what...")
        continue
    elif sysput == 9:
        clear()
        login()
        continue
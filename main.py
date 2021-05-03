### IMPORTS ###
import sys
import time
import random
from os import system, name

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
"""))
    except ValueError:
        clear()
        continue
    if sysput == 1:
        clear()
        continue
    elif sysput == 2:
        clear()
        continue
    elif sysput == 3:
        clear()
        continue
    elif sysput == 4:
        clear()
        continue
    elif sysput == 5:
        clear()
        continue
    elif sysput == 6:
        clear()
        input("You are now dead. Congradulations! Now what...")
        continue
import sys
import time
        
def print_slow(str):
    for char in str:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
def game():
    print_slow(f"{name}, Would you like to play a game? (yes/no) ")
    while True:        
        answer = (input())
        answer = answer.lower()
        if answer == "yes":
            print_slow("Welcome to the game\n")    
            print_slow(f"You are {name}. It is just turned 9 oclock and, after a long day at work, you have found yourself drifting off on the sofa. All of a sudden you are jolted awake by the sound of ringing. You fumble around the cushions \nlooking for your phone, but don't get to it in time before the call cuts off. The phone screen shows no caller ID. You shrug it off, assuming it was somebody trying to sell you something.\n")
            print_slow("The phone rings again. What do you do?(answer/ignore)\n")
            phone()
            break
        
        elif answer =="no":
            print_slow("Okay maybe another Time")
            break
                     
        else:
            print_slow("That is not a valid responce, try again ")  
def phone():
    while True:        
        answer = (input())
        answer = answer.lower()
        if answer == "answer":
            door()
            break
        
        elif answer == "ignore":
            print_slow("You turn your phone on silent and switch on the TV. You never pick up your phone for withheld numbers, it's always robots trying to scam you. You spend the rest of the night watching a show about truck drivers working in dangerous conditions. Hey, it passes the time.\n")
            print_slow("Thank you for... not playing the game!")
            break
        else:
            print_slow("That's not a valid repsonce, try again  ")
def door():           
    print_slow("""Confused as to why they rang back, you answer the phone. "Hello?" "You hear your voice echo back to you on the other end. "....." "No answer. "Listen if you're trying to sell me something then I'm not interested!" "You say before hangingup.\n""")
    print_slow("As soon as you press the red button on your phone screen you hear a loud, urgent banging on your front door. The noise makes you jump and nearly drop your phone. You stand up as the knocking gets louder.\n")
    print_slow("Nobody would call round at this time of night... What do you do?(open the door/dont open)\n")
    
    while True:        
        answer = (input())
        answer = answer.lower()
        if answer == "open the door":
            print_slow("You open the door")
            break
        
        elif answer =="dont open":
            print_slow("As you go to turn the latch and unlock the door a sense of dread suddenly washes over you. You're not sure why, but something in you is telling you not to answer the door. You turn away from the door as the phone begins to ring once \nagain.(answer/ignore)\n")
            phone()
            break
                     
        else:
            print_slow("That is not a valid responce, try again ")  
name = print_slow("What is your name? ")
name = input("")
game()

import sys
import time
        
def print_slow(str):
    for char in str:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
def kitchen():
    global knife
    print_slow("You read the note and it says to enter the kitchen. You enter the kitchen, you see a cupboard in the distance, what do you do? (Search cupboard/Search kitchen) ")
    answer = (input())
    answer = answer.lower()
    while True:
        if answer == "search kitchen":
            if knife == 0:
                knife =+ 1
                print_slow("you search the kitchen and find a knife\n")
                print_slow("What do you want to do (Search kitchen/Search cupboard) ")
                answer = (input())
            else:
                print_slow("you search around the kitchen again and couldn't find anything\n")
                print_slow("What do you want to do (Search kitchen\Search cupboard) ")
                answer = (input())
        elif answer =="search cupboard":
            if knife == 1:
                print_slow("You found a key")
                break
            else:
                print_slow("The ghost get's you, game over")
                break
        else:
            print_slow("this is not a valid responce, try again\n")
            answer = (input())
knife = 0
kitchen()

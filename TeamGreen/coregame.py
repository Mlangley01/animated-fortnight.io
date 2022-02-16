import sys
import time
import random
        
def print_slow(str):
    for char in str:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
def game():
    print_slow(f"{name}, Would you like to play a game? (Yes/No) ")
    while True:        
        answer = (input())
        answer = answer.lower()
        if "yes" in answer or answer == "y":
            phone()
            break
        
        elif answer =="no" or answer == "n":
            print_slow("Okay maybe another Time")
            break
                     
        else:
            print_slow("That is not a valid responce, try again\n")  
def phone():            
    print_slow("Welcome to the game\n")    
    print_slow(f"You are {name}. It is just turned 9 oclock and, after a long day at work, you have found yourself drifting off on the sofa. All of a sudden you are jolted awake by the sound of ringing. You fumble around the cushions \nlooking for your phone, but don't get to it in time before the call cuts off. The phone screen shows no caller ID. You shrug it off, assuming it was somebody trying to sell you something.\n")
    print_slow("The phone rings again. What do you do?(answer/ignore)\n")
    while True:        
        answer = (input())
        answer = answer.lower()
        if "answer" in answer:
            door()
            break
        
        elif "ignore" in answer:
            print_slow("You turn your phone on silent and switch on the TV. You never pick up your phone for withheld numbers, it's always robots trying to scam you. You spend the rest of the night watching a show about truck drivers working in dangerous conditions. Hey, it passes the time.\n")
            print_slow("Thank you for... not playing the game!\n")
            start_over()
            break
        else:
            print_slow("That's not a valid repsonce, try again\n")
def door():           
    print_slow("""Confused as to why they rang back, you answer the phone. "Hello?" "You hear your voice echo back to you on the other end. "....." "No answer. "Listen if you're trying to sell me something then I'm not interested!" "You say before hangingup.\n""")
    print_slow("As soon as you press the red button on your phone screen you hear a loud, urgent banging on your front door. The noise makes you jump and nearly drop your phone. You stand up as the knocking gets louder.\n")
    print_slow("Nobody would call round at this time of night... What do you do?(open the door/dont open)\n")
    
    while True:        
        answer = (input())
        answer = answer.lower()
        if answer == "open the door" or answer == "open" or answer == "open door":
            print_slow("You open the door\n")
            note()
            break
        
        elif "dont" in answer:
            print_slow("As you go to turn the latch and unlock the door a sense of dread suddenly washes over you. You're not sure why, but something in you is telling you not to answer the door. You turn away from the door as the phone begins to ring once \nagain.(answer/ignore)\n")
            phone()
            break
                     
        else:
            print_slow("That is not a valid responce, try again\n")  
def note():
    print_slow("You see the note inside the house, do you go in to read the note or call the police? (note/police) \n")
    while True:
        answer = (input())
        answer = answer.lower()
        if "note" in answer:
            kitchen()
            break
        elif "police" in answer:
            print_slow("Bad ending")
            start_over()
            break
        else:
            print_slow("This is not a valid respose, try again\n")
def kitchen():
    global knife
    print_slow("You read the note and it says to enter the kitchen. You enter the kitchen, you see a cupboard in the distance, what do you do? (Search cupboard/Search kitchen) \n")
    answer = (input())
    answer = answer.lower()
    while True:
        if "kitchen" in answer:
            if knife == 0:
                knife =+ 1
                print_slow("you search the kitchen and find a knife\n")
                print_slow("What do you want to do (Search kitchen/Search cupboard) ")
                answer = (input())
            else:
                print_slow("you search around the kitchen again and couldn't find anything\n")
                print_slow("What do you want to do (Search kitchen\Search cupboard) ")
                answer = (input())
        elif "cupboard" in answer:
            if knife == 1:
                print_slow("You found a key, ")
                loft()
                break
            else:
                print_slow("The ghost get's you, game over")
                start_over()
                break
        else:
            print_slow("this is not a valid responce, try again\n")
            answer = (input())
        
def loft():
    print_slow("After leaving the kitchen, you hear a noise in the loft,Do you want to leave the house or enter the loft? (leave/loft) \n")
    while True:    
        answer = (input())
        answer = answer.lower()
        if "leave" in answer:
            print_slow("Bad ending")
            break
        elif "loft" in answer:
            battle()
            break
        else:
            print_slow("This is not a valid repsponce, try again\n")
def battle():
    print_slow("You enter the loft and the ghost appears, do you fight or flee (Fight/Flee) \n")
   
    while True:    
        answer = (input())
        answer = answer.lower()
        if "fight" in answer:
            random_number = random.randint(0,1)
            if random_number == 1:
                print_slow("Bad ending")
                break
            else:
                print_slow("Good ending")
                break
        elif "flee" in answer:
            print_slow("bad ending")
            break
        else:
            print_slow("This is not a valid repsonce, try again\n")
def start_over():
    print_slow("Would you like to start over? (Yes/No) ")
    while True:
        answer = (input())
        answer = answer.lower()
        if "yes" in answer or answer == "y":
            phone()
            break
        if answer == "no" or answer == "n":
            print_slow("Have a nice day!")
            break
name = print_slow("What is your name? \n")
name = input("")
knife = 0
game()

import sys
import time
import random
        
def print_slow(str):
    for char in str:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
def battle():
    print_slow("You enter the loft and the ghost appears, do you fight or flee (Fight/Flee) ")
    answer = (input())
    answer = answer.lower()
    while True:
        if "fight" in answer:
            answer == random.randint(1,2)
            if answer == 1:
                print_slow("Bad ending")
                break
            else:
                print_slow("Good ending")
                break
        elif "flee" in answer:
            print_slow("bad ending")
            break
        else:
            print_slow("This is not a valid repsonce, try again")
battle()
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
    ans1 = (input())
    answer = ans1.lower()
    while True:
        if answer in ans1==(f"fight"):
            ans1 == random.randint()
            if ans1 == 1:
                print_slow("Bad ending")
                break
            else:
                print_slow("Good ending")
                break
        elif answer in ans1==(f"flee"):
            print_slow("bad ending")
            break
        else:
            print_slow("This is not a valid repsonce, try again")
battle()
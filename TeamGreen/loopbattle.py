import time
import sys
import random




def print_slow(str):
    for char in (str):
        time.sleep(0.5)
        sys.stdout.write(char)
        sys.stdout.flush()
        

print_slow(r"""

# insert any text here for slow word 


""" ) 
       
def battle():
    print("You enter the loft and the ghost appears, do you fight or flee (Fight/Flee)\n ")
    answer = (input())
    answer = answer.lower()
   
    while True:
        if "fight" in answer:
            random_number = random.randint(0,1)
            if random_number == 1:
                print_slow("\nBad ending"*13)
                break
            else:
                print_slow("\nGood ending")
                break
        elif "flee" in answer:
            print_slow("\nbad ending"*13)
            break
        else:
            print_slow("\nThis is not a valid repsonce, try again")
battle()
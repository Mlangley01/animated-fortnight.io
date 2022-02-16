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

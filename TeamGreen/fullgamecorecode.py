import sys
import time
import random
bad_ends =(r""" 
                                           .""--..__
                     _                     []       ``-.._
                  .'` `'.                  ||__           `-._
                 /    ,-.\                 ||_ ```---..__     `-.
                /    /:::\\               /|//}          ``--._  `.
                |   |:::::||              |////}                `-. \
                |   \:::::||             //'///                    `.\
                |    |::::||            //  ||'                      `|
                /    |::://        _,-//\  ||
               /`    |:::|`-,__,-'`  |/  \ || You Have met
             /`  |   |'' ||           \   |||    with a Ghostly Demise !!!
           /`    \   |   ||            |  /||   MWAAAAAHHHH!!!!!       
         |`       |  |   |)            \ | ||
        |          \ |   /      ,.__    \| ||
        /           `         /`    `\   | ||
       |                     /        \  / ||
       |                     |        | /  ||
       /         /           |        `(   ||
      /          .           /          )  ||
     |            \          |             ||
    /             |          /             ||
   |\            /          |              ||
   \/`-._       |           /              ||
    //   `.    /`           |              ||
   //`.    `. |             \              ||
  ///\ `-._  )/             |              ||
 //// )   .(/               |              ||
 ||||   ,'` )               /              ||
 ||||  /                    /              || 
 `\\` /`                    |              || 
     |`                     \              ||  
    /               |^         |           ||  
  /`                 |\         \          ||  
/`                    |\        |          ||    
`-.___,-.      .-.        ___,'            ||
         `---'`   `'----'`
         """)
             
note1= (r""" 
    ______________________________
  / \                             \.
 |   |                            |.
  \_ |  My name is Jack Daniels   |.
     |                            |.
     |  I am an old friend of     |.
     |  of your parents.          |.
     |                            |.
     |  I am trapped at the       |.
     |  enclosed address, I need  |.
     |  your help to get out.     |.
     |  Please, come get me       |.
     |  before midnight tonight.  |.
     |                            |.
     |  You're my only hope!      |.
     |                            |.
     |   _________________________|___
     |  /                            /.
     \_/____________________________/.
""")
note2=(r"""
    ______________________________
  / \                             \.
 |   |                            |.
  \_ |                            |.
     |     Cheers for that!       |.
     |                            |.
     |    I've been stuck here    |.
     |     for 20 years and I     |.
     |   wasn't myself anymore.   |.
     |                            |.
     |   I hope the contents of   |.
     |    this pouch will help    |.
     |   make up for my actions   |.
     |                            |.
     |   -Jack                    |.
     |   _________________________|___
     |  /                            /.
     \_/____________________________/.
""")
sharps =(r"""
                                
 __,,..,^            _,.--''------'' ||   _____  ______________`''--._
 \      `\   __..--''                ||  /::: / /::::::::::::::\      `\
  \       `''                        || /____/ /___ ____ _____::|    .  \
   \                          ______ ||           `    `     \_|   ( )  |
    `.                       /`     `\\ ,,''`'- ,.----------.._     `   |
      `.                     |        ,'       `               `-.      |
        `-._                 \                                    ``.. /
            `---..............>
This knife looks pretty handy 
I wonder what else I'll find in this creepy house ?.
""")
phone_pic =(r"""
            _.._           
     __.--"" __ ""--.__    
   .'//   .-"  "-.   \\`,  
  : :'  .'.  :;  ,`.  `; ; 
 /; ;  /  T. $$ ,P  \  : : 
/: :  ;    T.:;,P    :  ; ;
)| | :      `  '      ; | |
`j | :.--------------.: | |
 ; ; |                | : :
 ; ; |                | : :
 | | |                | | |
 | | |                | | |
 : : |                | ; ;
 : : :________________: ; ;
  ; ;__    _...._    __: : 
  | ;  "-./ ,--, \,-"  : | 
  | '._   \ ;  : /   _.' | 
  :  __`-. `."",' .-'__  ; 
   ;`.__> `.J__L.' <__.':  
   ;.--._   .--.   _.--,:  
   |`.__.' `.__.' `.__.'|  
   |.--._   .--.   _.--,|  
   |`.__.' `.__.' `.__.'|  
   |.--._   .--.   _.--,|  
   ;`.__.' `.__.' `.__.':  
  : .--._   .--.   _.--, ; 
  ; `.__.' `.__.' `.__.' : 
  ;                      : 
  '--..__          __..--' 
         ----------
""")
key = (r""")         
          .---.
         /    |\________________
        | ()  | ________   _   _)
         \    |/        | | | |
          `---'         "-" |_|
""")
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
    print(phone_pic)
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
            note()
            break
        
        elif "dont" in answer:
            print_slow("As you go to turn the latch and unlock the door a sense of dread suddenly washes over you. You're not sure why, but something in you is telling you not to answer the door. You turn away from the door as the phone begins to ring once \nagain.(answer/ignore)\n")
            phone()
            break
                     
        else:
            print_slow("That is not a valid responce, try again\n")  
            
def note():
    print_slow(f"""You turn the latch to the door and pull it open. There's nobody there, just a cardboard box on your doorstep. That's weird, you could've sworn the knocking stopped right as you turned the latch- You take a closer look at the box. It has a label that has "{name}, OPEN IN PRIVATE" in big red letters tied to it. You know you should be suspicious of a strange parcel dropped on your doorstep, but there's a niggling feeling in the back of your mind that makes your curiosity take over.""")
    print_slow("You pick up the box and head back inside. Inside the box is a note and a photo of a house with an address scribbled on the back")
    print(note1)
    print_slow("Your mind is spinning with questions, but you can't help but feel drawn to the house in the photo. You're sure you've seen it before, the address isn't too far from where you grew up. You know deep down that this is all very suspicious, any sensible person would call the police. But....")
    while True:
        answer = (input())
        answer = answer.lower()
        if "note" in answer:
            kitchen()
            break
        elif "police" in answer:
            print_slow("You decide that some things just aren't worth it. This is probably just a prank, but it could be something way more dangerous. You pull your phone out and type in 999.")
            print_slow("Over the next couple of days the police come, ask you some questions and take the box and its contents as evidence. You explained to them that you don't know much, it just turned up on your doorstep one night. Nothing comes of the mysterious note and life carries on as normal, the events of that night eventually fading away into memory.")
            print_slow("Congratulations, you were sensible and lived a long, normal life with absolutely 0 paranormal activity!")
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
                print(sharps)                                
                print_slow("What do you want to do (Search kitchen/Search cupboard) ")
                answer = (input())
            else:
                print_slow("you search around the kitchen again and couldn't find anything\n")
                print_slow("What do you want to do (Search kitchen\Search cupboard) ")
                answer = (input())
        elif "cupboard" in answer:
        
            if knife == 1:
                print_slow("You found a key, ")
                print_slow(key) 
                loft()
                break
            else:
                print_slow("The ghost get's you, game over")
                print(bad_ends)
                start_over()
                break
        else:
            print_slow("this is not a valid responce, try again\n")
            answer = (input())
        
def loft():
    print_slow("As you head back out of the kitchen you notice that the key seems like it'd fit into the lock on the door. Before you can test it out you hear a blood curdling scream coming from the upper floor of the house, followed by a loud bang. You jump and nearly drop the key. Whoever it is sounds like they're in a lot of pain. Your hands are shaking and you find yourself fighting between two choices. What should you do? (leave/check upstairs)")
    while True:    
        answer = (input())
        answer = answer.lower()
        if "leave" in answer:
            print_slow("Your hands shaking, you get the key into the lock on the door, twist and- CLICK! You swing the door wide and sprint for your car, the sounds of screams following you from the house. You jump in the driver's seat and take off down the road just as the apparition burst from the door heading straight for your car.")
            print_slow("You narrowly avoided the ghost's attack and made your way home.")
            print_slow("""Images of the spirit's face flashed in your mind keeping you awake. You sat on your bed clutching the knife and staring at your bedroom door until morning came. The next day your co-workers asked what was wrong. "You look like you've seen a ghost" one of them commented. If only they knew...""")
            print_slow("Congratulations! You got out of there just in time and are left with lasting psychological damage. Oh well, could've been worse!")
            start_over()
            break
        elif "loft" in answer or "upstairs" in answer:
            print_slow("You want to get out of there, but you can't just leave knowing someone else is in here. You stuff the old key in your pocket and run up the stairs in the direction of the noise.When you reach the top of the stairs you hear more clearly that the sound is coming from up in the attic. A ladder is propped up against the wall, but the latch appears to be locked.You climb up the ladder and pull out the old key. The lock clicks open and you enter the loft.")
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
                print_slow(bad_ends)
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
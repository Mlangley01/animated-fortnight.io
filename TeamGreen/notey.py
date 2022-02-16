import time
import sys





print("Hello")


def print_slow(str):
    for char in (str):
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()


def print_slow1(str):
    for char in (str):
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()


print_slow(r"""

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
 


""" )

print(r"""                                 
 __,,..,^            _,.--''------'' ||   _____  ______________`''--._
 \      `\   __..--''                ||  /::: / /::::::::::::::\      `\
  \       `''                        || /____/ /___ ____ _____::|    .  \
   \                          ______ ||           `    `     \_|   ( )  |
    `.                       /`     `\\ ,,''`'- ,.----------.._     `   |
      `.                     |        ,'       `               `-.      |
        `-._                 \                                    ``.. /
            `---..............>
This knife looks pretty handy 
I wonder what else I'll find in this creepy house ?.""")


print_slow1("""why art stored as a variable in code\nAfter researching ascii art files and how they could be used in the terminal\n
I quickly realised inputing each art piece took up vast amounts of terminal space when writing the game code\n
so I tried creating seperate variables to call at required points in my code rather than having to input each piece over and over again.\n
I did experiment further by storing my art= variables in a seperate file with independent time.sleep settings from the main game code\n 
which allowed me to import the file into my code which cleaned up the games code engine by storing the art files in a seperate container   


""")
    
#ansi
def main(): #declare main class here is refrenced before anything else
    guessing()  #Call Class guess running function inside

def guessing():
    countin = 0 #set counter variable and initialise
    while countin < 3:  #whilst counter less than 3 do till else
        guess = input('Guess a number \n:-')
        countin = countin + 1   #increase counter
        if guess == '1234': #input variable match literal could be dynamic i.e a a dictionar search
            print ('welll done')
            countin =4  #Ugly way but escaped while clause
            break
        else:
            exit

    else:
        print ('too many guesses')
        
guessing()
if __name__ == "__main":
    main()
    
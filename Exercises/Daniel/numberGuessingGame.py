import random 



def guessingGame():
    
    print("Welcome to the number guessing game, you have five tries to guess the correct number between 1 - 1000.")
    print("--------------------------------------------------------------- \n")
    
    randomNumber = random.randrange(1,1000)
    

    userInput = int(input("Type your guess: "))
    
        
        

    count = 0
    
    play = True
    
    while play:
        if userInput < 1 or userInput > 1000:
            print("The number you put in is not in the range")
            guessingGame()
        else:
            if count >= 4:
                print(f"You have failed to guess the number. The number was {randomNumber} Do you want to play again?")
                userInput = int(input("1 for yes, any other number for no: "))
                if userInput == 1:
                    guessingGame()
                else: 
                    print("Okey bye!")
                    play = False
                
            else:
                if userInput == randomNumber:
                    count += 1
                    print(f"Correct!!! You guessed it in {count} tries. Do you want to play again?")
                    userInput = int(input("1 for yes, any other number for no: "))
                    
                    if userInput == 1:
                        guessingGame()
                    else: 
                        print("Okey bye!")
                        play = False
                    
                else:
                    count += 1
                    if userInput < randomNumber: 
                        print(f"Wrong! The number is too low. You have {5 - count} tries left.")
                        userInput = int(input("Type your guess: "))
                    
                    elif userInput > randomNumber: 
                        print(f"Wrong! The number is too high. You have {5 - count} tries left.")
                        userInput = int(input("Type your guess: "))
                    
guessingGame()

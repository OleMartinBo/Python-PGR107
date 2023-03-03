from random import randint


def game() :
    
#Variabler 
    value = randint(1,1000)
    counter = 0
    attempts = 5
    
#Logikk for spillet 
    while counter != 5 :
        
        userInput = int(input("Enter a number: "))
        
        if userInput == value :
            print("Congratulation! You guessed the number in:", counter ,"attempt(s)”")
            print("------------------------------------------------------------------")
            print(" ")
            break
        elif userInput < value :
            print("The number is Higher")
            print("-------------------")
            print(" ")
        elif userInput > value :
            print("The number is lower")
            print("-------------------")
            print(" ")
        
        counter += 1
        print("You got:",attempts - counter ,"attempts left")
        print("-------------------")
        print(" ")
        
        if counter == 5 :
            print("Sorry!! You did not manage to guess the number.\nYou have reached the guessing limit", counter,".\nThe number was:", value)
            print("-------------------------------------------------")
            print(" ")
            
            
#Menyen for spillet 
def menu():
    
    print("Welcome to Number Guessing Game!")
    print("--------------------------------")
    
    while True:
        choice = input("Enter YES to play again or NO to quit: ")
        print("-----------------------------------------------------")
        print(" ")

        if choice.lower() == "yes":
            game()
        elif choice.lower() == "no":
            print("Goodbye!")
            break
        else:
            print("Not a valid input! Enter YES or NO")

            
#Kjører programmet 
menu()
            
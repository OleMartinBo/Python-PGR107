from random import randint


def game() :
    
#Variabler 
    value = randint(1,1000)
    counter = 0
    
#Logikk
    while counter != 5 :
        
        userIput = int(input("Enter a number: "))
        
        if userIput == value :
            print("Congratulation! You guessed the number in:", counter ,"attempt(s)”")
            print("------------------------------------------------------------------")
            print(" ")
            break
        elif userIput < value :
            print("The number is Higher")
            print("-------------------")
            print(" ")
        elif userIput > value :
            print("The number is lower")
            print("-------------------")
            print(" ")
        
            
        counter += 1
        if counter == 5 :
            print("Sorry!! You did not manage to guess the number.\nYou have reached the guessing limit.\nThe number was:", value)
            print("-------------------------------------------------")
            print(" ")
            
            


game()

def menu():
    choice = str(input("Enter YES to play again or NO to quit: "))
    
    while choice.lower or choice.upper == "yes" :
        game()
    
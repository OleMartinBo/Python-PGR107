import random 


def playGame(): 
    number = random.randint(1,1000)
    attempts = 5

    while attempts > 0: 
        guess = int(input("Guess the number between 1 and 1000: "))
        if guess == number : 
            print("Congratulation! You guessed the number in ", 5- attempts + 1, "attempt(s)")
            return True 
        elif guess < number : 
            print("The number is to low. ")
        else : 
              print("The number is too high.")
        attempts -= 1
        print("You have", attempts, "attempt(s) left.")
    print("Sorry!! You did not manage to guess the number. You have reached the guessing limit. The number was:", number)
    return False
    

def main():
    playAgain = True

    while playAgain:
        playGame()
        answer = input("Do you want to play again? (yes/no) ").lower()
        playAgain = (answer == "yes")

if __name__ == "__main__":
    main()




        


        










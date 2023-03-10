
def vowelCheck():
        vowels = "aeiouAEIOU"
        userInput = input("Enter a letter: ")
        if userInput in vowels:
            print("This is a vowel") 
        elif userInput.lower() == "y":
            print("Y is sometimes a vowel, and sometimes not.")    
        else:
            print("This is a vowel")
            

# vowelCheck()

#Oppgave 2

def determineSides():
    userInput = int(input("How many sides does your shape have? Write a number between 3-10: "))
    if userInput == 3:
        print(f"Triangle")
    elif userInput == 4:
        print("Square")
    elif userInput == 5:
        print("Pentagon")
    elif userInput == 6:
        print("Hexagon")
    elif userInput == 7:
        print("Hectagon")
    elif userInput == 8:
        print("Octagon")
    elif userInput == 9:
        print("Nonagon")
    elif userInput == 10:
        print("Decagon")
    else:
        print("You have entered the wrong input.")

# determineSides()


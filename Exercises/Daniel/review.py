
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

#Oppgave 3

def determineDays():
    userInput = input("What month? ")
    if userInput.lower() == "january" or userInput.lower() == "march" or userInput.lower() == "may" or userInput.lower() == "july" or userInput.lower() == "august" or userInput.lower() == "october" or userInput.lower() == "desember":
        print("31 days")
    elif userInput.lower() == "febuary":
        print("Febuary can be either 28 or 29 days.")
    elif userInput.lower() == "april" or userInput.lower() == "juni" or userInput.lower() == "september" or userInput.lower() == "november":
        print("30 days")
    else:
        print("Your input is wrong idiot")

# determineDays()

#Oppgave 4

def whatTriangle():
    userInput1 = int(input("Write the lenght of side 1: "))
    userInput2 = int(input("Write the lenght of side 2: "))
    userInput3 = int(input("Write the lenght of side 3: "))
    if userInput1 == userInput2 and userInput1 == userInput3:
        triangle = "Equilateral"
    elif userInput1 == userInput2 or userInput2 == userInput3 or userInput1 == userInput3:
        triangle = "Isoseles"
    else:
        triangle = "Scalene"
    print(f"Your triangle is {triangle}")

whatTriangle()
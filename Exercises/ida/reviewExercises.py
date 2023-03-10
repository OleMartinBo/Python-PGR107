#Task 1 

# vowels = "aeioAEIOU"
# alphabetLetter = input("Enter a letter from the alphabeth: ")

# if alphabetLetter in vowels:
#     print("The letter is a vowelel")
# elif alphabetLetter == "y":
#     print("sometimes y is a vowel, and sometimes y is a consonant")
# else:
#     print("the letter is a consonant")

#Task 2

def task2Shapes():
    userInput = int(input("Enter number of sides from 3-10:"))
    if userInput == 3:
        print(f"The shape of side {userInput}, is a rectangle")
    elif userInput == 4:
        print(f"The shapeof side {userInput}, is a rectangle/square")
    elif userInput == 5:
        print(f"the shape of side {userInput}, is a pentagon")
    elif userInput == 6:
        print(f"The shape of side {userInput}, is a hexagon")
    elif userInput == 7:
        print(f"The shape of {userInput}, is a Heptagon")
    elif userInput == 8:
        print(f"The shape of {userInput}, is Octagon")
    elif userInput == 9:
        print(f"The shape of {userInput}, is a nonagon")
    elif userInput == 10:
        print(f"The shape of {userInput}, is a decagon")
    else:
        print("Write a shape of sides 3-10")

# task2Shapes()


#Task 3

def task3Month():
    userInput = input("Enter a month: ")
    if userInput == "April" or userInput == "June" or userInput == "September" or userInput == "November":
        print(f" {userInput} month have 30 days")
    elif userInput == "January" or userInput == "March" or userInput == "May" or userInput == "July" or userInput == "October" or userInput == "December":
        print(f"{userInput} month have 31 days")
    elif userInput == "February":
        print(f"{userInput} month have 28/29 days")
    else:
        print("Write a valid input")

#task3Month()

#task 4


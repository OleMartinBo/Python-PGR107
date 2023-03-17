
import random


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

# whatTriangle()

#oppgave 5
def defineSeason():
    userMonth = input("What month? ")
    userDate = int(input("What date? "))
    season = ""
    if userMonth.lower() == "desember" or userMonth.lower() == "january" or userMonth.lower() == "febuary":
        if userMonth.lower() == "desember" and userDate < 21:
            season = "Autumn"
        else:
            season = "Winter"
    elif userMonth.lower() == "march" or userMonth.lower() == "april" or userMonth.lower() == "may":
        if userMonth.lower() == "march" and userDate < 21:
            season = "Winter"
        else: 
            season = "Spring"
    elif userMonth.lower() == "june" or userMonth.lower() == "july" or userMonth.lower() == "august":
        if userMonth.lower() == "june" and userDate < 21:
            season = "Spring"
        else:
            season = "Summer"
    elif userMonth.lower() == "september" or userMonth.lower() == "october" or userMonth.lower() == "november":
        if userMonth.lower() == "august" and userDate < 21:
            season = "Summer"
        else:
            season = "Autumn"
    else: 
        print("Your input is wrong IDIOT")
    
    print(f"{userDate} {userMonth} is in: {season}")
    
#defineSeason()

def generateRaise():
    raiseBase = 2400
    newRaise = 0
    message = ""
    
    rate = input("Is your interest 0.0 0.4 or 0.6? ")
    if float(rate) == 0.0:
        newRaise = raiseBase * 0.0
        message = "Your work is very bad, shame on you!"
    elif float(rate) == 0.4:
        newRaise = raiseBase * 0.4
        message = "Your work is ok"
    elif float(rate) == 0.6:
        newRaise = raiseBase * 0.6
        message = "Excellent job!"
    else:
        message = "Your entry is unvalid"
    
    return print(f"{message} Your raise is: {newRaise}")

# generateRaise()

def determineSalary():
    userHours = float(input("Enter your hours worked: "))
    BASE_SALARY = 8
    BONUS_SALARY = 12
    userSalary = 0
    extraSalary = 0
    if userHours < 0:
        print("You worked less than 0 hours?")
    elif userHours > 40:
        overForty = userHours - 40
        userSalary = 320 + overForty * BONUS_SALARY
    else: 
        userSalary = userHours * BASE_SALARY
    
    return userSalary

# print(f"Your salary is: {determineSalary()}$")

def isSenior():
    userInput = input("Write s for senior: ")
    output = ""
    
    if userInput.lower() == "s":
         output = "The salary for a senior developer is 800$ a week"
    else: 
        output = "The salary of a junior developer is 375$ a week"
    
    
    return output

# print(isSenior())
def whileLoop():
    x = 1
    while x <= 5:
        f = 1 + x + (x**2)/2 + (x**3)/6 + (x**4)/24
        print(f"x = {x} --> f(x) = {f: 0.2f}")
        x += 1

# whileLoop()

def forLoop():
    x = 6
    for i in range(1,x):
        f = 1 + i + (i**2)/2 + (i**3)/6 + (i**4)/24
        print(f"x = {i} --> f(x) = {f: 0.2f}")
        
# forLoop()

def coinToss():
    userInput = int(input("Write how many times the coin toss should happen: "))
    heads = 0
    tails = 0
    for i in range(1, userInput+1):
        number = random.randint(1,2)

        if number == 1:
            heads = heads + 1
        elif number == 2:
            tails = tails + 1
        else: 
            print("Wrong input")
        
    return print(f"Number of heads: {heads}\nNumber of tails: {tails}")
    
# coinToss()

def determineVolume():
    r = float(input("Enter radius: "))
    PI = 3.14
    volume = 4/3 * PI * r**3
    
    return volume

print(f"The volume is: {determineVolume()}")


    
    
        
    
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

from random import randint


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

""" 
equilateral: samme side 
isosceles: to sider er like
scalene: alle sidene er ulike
"""

def task4Triangle ():
    sideA = float(input("Enter side A of triangle: "))
    sideB = float(input("Enter side B of triangle: "))
    sideC = float(input("Enter side C of triangle: "))
    if sideA and sideB == sideC:
        print(f"A triangle, with side {sideA}, {sideB}, and {sideC}, is an equilateral")
    elif sideA == sideB or sideB == sideC or sideA == sideC:
        print(f"A triangle, with side {sideA}, {sideB}, and {sideC}, is an is an isosceles")
    else:
        print(f"A triangle, with side {sideA}, {sideB}, and {sideC}, is an scalene")

#task4Triangle()

#task 5

def task5Month():
    month = input("Enter a month: ")
    day = int(input("Enter a day: "))

    if day < 1 or day > 31:
        print("Enter valid day of month.")
   
    else: 
        if month == "January" or month == "February":
            print("The season is winter")
        elif month == "March" and day < 20:
            print("The season is winter")
        elif month == "March" and day >= 20:
            print("the season is Spring")
        elif month == "April" or month == "May":
            print("The season is Spring")
        elif month == "June" and day < 21:
            print("The season is Spring")
        elif month == "June" and day >= 20: 
            print("The season is Summer")
        elif month == "July" and month == "August":
            print("The season is summer")
        elif month == "September" and day < 22:
            print("The season is summer")
        elif month == "September" and day >=22:
            print("The season is Fall")
        elif month == "October" and month == "November":
            print("the season is Fall")
        elif month == "December" and day >= 21:
            print("The season is winter")
        elif month == "December" and day < 21:
            print("the season is Fall")
        else:
            print(f" {month} is a invalid input")

#task5Month()


#task6

def zodiac(year):
    animals = ['monkey', 'rooster', 'dog', 'pig', 'rat', 'ox', 'tiger', 'hare', 'dragon', 'snake', 'horse', 'sheep']
    index = year % 12
    return animals[index]

def task6Animals():

    year = int(input("Write a year to see animals associated with that year: "))

    if year < 0:
        print("Enter valid year")
    else:
        animal = zodiac(year)
        print(f"the animal associated with {year} is {animal}")
        

#task6Animals()


#task 7


def task7Employees():

    RAISE = 2400.00
   
    rating = float(input("Enter raiting: "))
    if rating == 0:
        emplyeeRaise = RAISE * rating
        print("Unacceptable performance")
        print(f"you wil receive a raise of {emplyeeRaise}")
    elif rating == 0.4:
        emplyeeRaise = RAISE * rating
        print("acceptable performance")
        print(f"you wil receive a raise of {emplyeeRaise}")
    elif rating >= 0.6:
        emplyeeRaise = RAISE * rating
        print("Meritorious performance")
        print(f"you wil receive a raise of {emplyeeRaise}")
    else:
        print("enter valid rating")


#task7Employees()

#Task8

def task8():
    userInput = float(input("Enter hours worked to see salary: "))

    if userInput < 0:
        print("invalid input.")
    elif userInput <= 40:
        salary = userInput * 8
        print(f"Your salary are {salary} dollars")
    else:
        salary = 320 + (userInput - 40) * 12
        print(f"Your salary are {salary} dollars")

#task8()

SENIOR = 800
JUNIOR = 375

def task9():
    status = input("Enter status of the salesperson (s or j): ")

    if status.lower() == "s":
        print(f"the salary of the senior is {SENIOR} dollar per week")
    elif status.lower() == "j":
        print(f"the salary of the junior is {JUNIOR} dollar per week")
    else:
        print("Enter valid input")

#task9()

#task 10 - while loop and for loop

def task10WhileLoop():

    x = 1
    while x <= 5:
        y = 1 + x + (x **2)/2+ (x**3)/6 + (x **4)/24
        print(f" x = {x} --> f(x) = {y :.2f}")
        x = x + 1

        
def task10ForLoop():
    for x in range(1, 6):
        y = 1 + x + (x **2)/2+ (x**3)/6 + (x **4)/24
        print(f" x = {x} --> f(x) = {y :.2f}")

#task10WhileLoop()
#task10ForLoop()

#task 11 

"""
tilfeldig tall og må da importere randint 
"""


def task11():
    head = 0
    tail = 0

    for i in range(1000):
        coin = randint(1,2)  #head =1 og tail =2
        if coin == 1: 
            head += 1
        else:
            tail += 1

    print(f"The number of heads are {head} and the number of tails are {tail}")

#task11()

#Task 12 

pi = 3.14

def task12():
    radius = float(input("Enter sphere radius: "))
    volume = volumeSphere(radius)
    print(f"volume of sphere with {radius : .0f} as a radius, is {volume : .2f}")

def volumeSphere(r):
    V = 4.0/3.0 * pi * r ** 3
    return V

#task12()

#task 13

def task13():
    x = float(input("Enter value of x: "))
    result = g(x)
    print(f"x = {x}, and the result of g(x) are: {result}")
    

def g(x):
    if x < 1:
        return -(x ** 2) + 4
    else:
        return 2* x - 1

task13()


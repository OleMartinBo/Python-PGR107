
#Oppgave 1
def vowel():
    
    userInput = str(input("Enter an string: "))
    
    if userInput in  "aeiouAEIOU" :
        print("There are vowels")
    elif userInput == "y" :
        print("Could be vowels or a Consonant")
    else :
        print("Consonant")

#vowel()

#Oppgave 2
def shapes(): 
    
    while True:
        choice = input("Enter YES for more shapes or NO to quit: ")
        print(" ")

        if choice.lower() == "yes":
            
                userInput = int(input("Enter a number of sides in integer: "))
                
                if userInput < 3 or userInput > 10 :
                    print ("There are no shapes under 3 sides or over 10 sides")
                elif userInput == 3 :
                    print("Triangle")
                elif userInput == 4 :
                    print("Square")
                elif userInput == 5 :
                    print("pentagon")
                elif userInput == 6 :
                    print("Hexagon")
                elif userInput == 7 :
                    print("Heptagon")
                elif userInput == 8 :
                    print("Octagon")
                elif userInput == 9 :
                    print("Nonagon")
                elif userInput == 10 :
                    print("Decagon")
                    
        elif choice.lower() == "no":
            print("Quiting...")
            break
        else:
            print("Not a valid input! Enter YES or NO")

#shapes()

#Oppgave 3
def month() :
    
    userInput = input("Enter a month: ")
    
    if userInput == "januar" or userInput == "mars" or userInput == "mai" or userInput == "juli" or userInput == "august" or userInput == "october" or userInput == "desember" :
        daysInMoth = 31
    elif userInput == "april" or userInput == "juni" or userInput == "september" or userInput == "november" :
        daysInMoth = 30
    elif userInput == "februar" :
        daysInMoth = "28 or 29"
    else :
        daysInMoth = 0
        
    if daysInMoth == 0 :
        print("There are no month")
    else :
        print(userInput,"has",daysInMoth,"days")
        
#month()

#Oppgave 4
def triangle():
    
    x = int(input("Enter lenght one: "))
    z = int(input("Enter lenght two: "))
    y = int(input("Enter lenght three: "))

    if x < 1 or z < 1 or y < 1 :
        print("There cant be anything under 1")
    else: 
        if x and z == y :
            shape = "equilateral" 
        elif x == z and y != x and z :
            shape = "isosceles"
        else :
            shape = "scalene"
            
        print("The shape you have is", shape)
        
        
    
#triangle()

#Oppgave 6
def animalYear() :
    
    year = int(input("Enter a year: "))
    
    if year < 0 :
        print("invalid year")
    else :
        if year % 12 == 8 :
            animal = "Dragon"
        elif year % 12 == 9 :
            animal = "snake"
        elif year % 12 == 10 :
            animal = "Horse"
        elif year % 12 == 11 :
            animal = "Sheep"
        elif year % 12 == 0 :
            animal = "Monkey"
        elif year % 12 == 1 :
            animal = "Rooster"
        elif year % 12 == 2 :
            animal = "Dog"
        elif year % 12 == 3 :
            animal = "Pig"
        elif year % 12 == 4 :
            animal = "Rat"
        elif year % 12 == 5 :
            animal = "Ox"
        elif year % 12 == 6 :
            animal = "Tiger"
        else :
            animal = "hare"
        
        print(year, "are the year of",animal)
        
#animalYear()

#Oppgave 7
def rating():
    
    inputValue = float(input("Enter value 0.0 or 0.4 or 0.6: "))
    
    if inputValue == 0.0 :
        value = "Unacceptable preformance"
    elif inputValue == 0.4 :
        value = "Acceptable preformance"
    elif inputValue >= 0.6 :
        value = "Meritorious preformance"
    else :
        value = ""
    
    if value == "" :
        print("Invalid")
    else :
        print("Your preformance is", value, "The raise you will have is", inputValue * 2400.00)
        
        
#rating()

#Oppgave 8

def salary():
    
    hours = int(input("Enter the hours worked: "))
    if hours < 0 :
        print("invalid")
    elif hours < 40 :
        salary = hours * 8
        print("Your salary is", salary)
    else :
        salary = 320 + (hours -40) * 12
        
    #print("Salary:", salary)
    
#salary()

#Oppgave 9
def salaryStatus() :
    
    #Variabler
    salaryValueSenior = 800
    senior = "s"
    
    salaryValueJunior = 375
    junior = "j"
    
    #Input
    charInput = input("Enter status s/j: ")
    
    #IF function
    if charInput.lower() == senior :
        print("The value of your salary is:", salaryValueSenior)
    elif charInput.lower() == junior :
        print("The value of your salary is:", salaryValueJunior)
    else :
        print("invalid")
        
#salaryStatus()

#Oppgave 10
def whileLoop() :
    
    x = 1
    while x <= 5 :
        #Lager ny variabel Y 
        y = 1 + x + (x ** 2) /2+ (x ** 3)/6 + (x ** 4)/24
        print("x =", x, "-->" "f",x ,"=", y)
        #Legger til 1 til x per runde opp til eller lik 5
        x = x + 1
        
#whileLoop()
    
    
def forLoop() :
    #Kjører fem ganger fram til den avslutter på 6 omgang
    for x in range(1, 6):
        y = 1 + x + (x ** 2)/2 + (x ** 3)/6 + (x ** 4)/24
        print(f"x = {x} --> f(x) = {y : .2f}")

#forLoop()

#Oppgave 11
def coinToss() :
    from random import randint
    
    heads = 0
    tails = 0
    count = 0
    
    while count < 1000 :
        coin = randint(1,2)
        if coin == 1 :
            heads = heads + 1 
        else :
            tails = tails + 1
        count = count + 1
    
    print("Heads=", heads,"\nTails=" , tails)
    
#coinToss()

#Oppgave 12
from math import pi

def program() :
    
    radius = int(input("Enter the radius: "))
    volume = sphere(radius)
    print("The volume of the sphere is", volume)
    
def sphere(r) :
    volume = (4/3) * pi * r ** 3
    return volume

#program()

#Oppgave 13
def main():
    x = float(input("Enter x: "))
    result = g(x)
    print(f"x = {x} --> g(x) = {result}")
    
def g(x):
    if x < 1:
        return -(x * x) + 4
    else:
        return 2 * x - 1
    
main()

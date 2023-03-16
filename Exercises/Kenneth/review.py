
#Oppgave 1 

letter = input("Enter a letter from alphabet: ").lower()
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("The letter is a vowel")
elif letter == "y": 
    print("Somtimes the letter y is a vowel, and sometimes it can be a consonant. ")
else: 
    print("The letter is a consonant")



#Oppgave 2 

numSides = int(input("Enter the number of sides (3-10) of the shape: "))

if numSides == 3: 
    print("The shape is a Triangle. ")
elif numSides == 4: 
    print("The shape is a Rectangle or a Square. ")
elif numSides == 5: 
    print("The shape is a Pentagon. ")
elif numSides == 6: 
    print("The shape is a Hexagon. ")
elif numSides == 7: 
    print("The shape is a Heptagon or Septagon. ")
elif numSides == 8: 
    print("The shape is an Octagon. ")
elif numSides == 9: 
    print("The shape is a nonagon or an ennagon.")
elif numSides == 10: 
    print("The shape is a decagon. ")
else: 
    print("Error: The number of sides must be between 3 and 10 ")


#oppgave3 

month = input("Enter the name of a month: ").lower()
if month == "january" or month == "march" or month == "may" or month == "july" == "august" or month =="december": 
    print("The month has 31 days. ")
elif month == "april" or month == "june" or month == "september" or month == "november":
    print(" The month has 30 days.")
elif month == "february": 
    print("Has 28 or 29 days. ")
else: 
    print("Invalid month names")


#Oppgave4

side1 = int(input("Enter the length of the first side: "))
side2 = int(input("Enter the length of the second side: "))
side3 = int(input("Enter the lenght of the third side: "))

if side1 == side2 == side3 : 
    print(" The Triangle is  an equilateral triangle. ")
elif side1 == side2 or side1 == side3 or side2 == side3: 
    print("The triangle is an isoscelses triangle. ")
else: 
    print("The triangle is a scalene triangle. ")

#Oppgave 5 

month = input("Enter the month ( January, February, March ect .. ): ").lower()
day = int(input("Enter a day (1-31): "))

if month == "december" and day >= 21 or month == "january " or (month == "february" or month == "march"  and day < 20): 
    season = "winter"
elif month == "march" and day >= 20 or month == "april " or  month == "may" or ( month == "june" and day <21): 
    season = "spring"
elif month == "june " and day >= 21 or month == "july" or month == "august" or (month == "september" and day < 22): 
    season = "summer"
elif month == "september" and day >= 22 or month == "october" or month == "november" or (month == "december" and day <20): 
    season = "fall (or atumn)"
else: 
    season = ("invalid date")

print("the season correspond to {} {} is {} ".format(month.capitalize(), day, season))



#Oppgave6 

year = int(input("Enter a year: "))

animals = ["Monkey","Rooster","Dog","Pig","Rat","Ox","Tiger","Hare","Dragon","Snake", "Horse","Sheep"]
index = (year-2000) % 12
animal = animals[index]

print("The animal for  the year" , year, "is", animal)
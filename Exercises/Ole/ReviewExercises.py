
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

#Oppgave 5
def seasons():
    
    inputMonth = input("Enter a month: ")
    inputDay = int(input("Enter a number: "))
    
    if inputDay < 1 or inputDay > 31 :
        print("there is no day out")
    else :
        if inputMonth == "januar" or inputMonth == "february" :
            season = "winter"
        elif inputMonth == "march" :
            if inputDay < 20 :
                season = "winter"
            else :
                season = "spring"
        elif inputMonth == "april" or inputMonth == "mai" : 
            season = "spring"
        elif inputMonth == "june" :
            if inputDay < 21 :
                season = "spring"
            else :
                season = "summer"
        elif inputMonth == "juli" or inputMonth == "august" :
            season = "summer"
        elif inputMonth == "september" :
            if inputDay < 22 :
                season = "summer"
            else :
                season = "fall"
        elif inputMonth == "october" or inputMonth == "november" :
            season = "fall"
        elif inputMonth == "desember" :
            if inputDay < 21 :
                season = "fall"
            else :
                season = "winter"
        else :
            inputMonth = ""
            
        
        if inputMonth != "" :
            print("The season is", season, "in month", inputMonth, inputDay)
        else :
            print("there where no valid month or day")

    
seasons()
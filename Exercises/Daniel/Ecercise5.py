# #Oppgave 1
# from math import sqrt
# def f(x):
#     return g(x) + sqrt(h(x))

# def g(x):
#     return 4 * h(x)

# def h(x):
#     return x * x + k(x) - 1

# def k(x):
#     return 2 * (x + 1)

# x1 = f(2)

# x2 = g(h(2))

# x3 = k(g(2) + h(2))

# x4 = f(0) + f(1) + f(2) 

# x5 = f(-1) + g(-1) + h(-1) + k(-1) 


# #Oppgave 2
# total = 1
# def factorial(number):
#     for number in range(1,userInput):
#         global total
#         total += total * number
        
        
#     return total
        

# userInput = int(input("Write a whole number: "))

# result = factorial(userInput)
# print("The factorial is:", result)

#Oppgave 3

# def integerPower(x, y):
#     total = userX
#     for num in range(1,y):
        
#         total *= x
    
#     return total

# userX = int(input("Write an integer: "))
# userY = int(input("Write a positive integer: "))


# result = integerPower(userX, userY)

# print(result)

# def multiple(x, y):
#     isMultiple = ""
#     if y % x == 0:
#         isMultiple = "%s" % str(x)+ "%s" % " is in fact a multiple of "+ "%s" % str(y)
#     else: 
#         isMultiple = "%s" % str(x)+ "%s" % " is in fact NOT a multiple of "+ "%s" % str(y)
#     return isMultiple
        
        

# userX = float(input("Write a number: "))
# userY = float(input("Write a number: "))

# result = multiple(userX, userY)

# print(result)

#oppgave 5



def celciusToFahrenheit(C):
    F = (9/5)*C + 32
    return F 

def fahrenheitToCelsius(F):
    C = (5/9)*(F-32)
    return C 

def menu():
    
    print("Enter 1 to convert from Celsius to Farhenheit")
    print("Enter 2 to convert from Farhenheit to Celsius")
    print("Enter a negative number to quit")
    userInput = input("You: ")
    while True:
        if int(userInput) <= 0:
            break
        
        if userInput == "1":
            celsius = float(input("Enter Celsius: "))
            print("%.2f %s %.2f %s" % (celsius, "degrees celsius is:", celciusToFahrenheit(celsius), "degrees fahrenheit")  )
        
        elif userInput == "2":
            fahrenheit = float(input("Enter Fahrenheit: "))
            print("%.2f %s %.2f %s" % (fahrenheit, "degrees Fahrenheit is:", fahrenheitToCelsius(fahrenheit), "degrees Celsius")  )
        else: 
            print("wrong input")
        print()
        print("Enter 1 to convert from Celsius to Farhenheit")
        print("Enter 2 to convert from Farhenheit to Celsius")
        print("Enter a negative number to quit")
        print()
        userInput = int(input("Enter 1 or 2: "))
        

menu()
 

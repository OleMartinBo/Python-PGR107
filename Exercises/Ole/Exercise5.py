# from math import sqrt
linebreak = "-" * 20

# #Oppgave 1 
# print("Oppgave 1")
# def f (x) :
#     return g(x) + sqrt(h(x)) 

# def g (x): 
#     return 4 * h (x) 

# def h (x): 
#     return x * x + k (x) - 1 
 
# def k (x): 
#     return 2 * (x + 1) 
 

# x1 = f (2) 
# x2 = g (h (2)) 
# x3 = k (g (2) + h (2)) 
# x4 = f (0) + f (1) + f (2) 
# x5 = f (-1) + g (-1) + h (-1) + k (-1) 

# print("X1 =", x1,"X2=", x2, "X3=", x3, "X4=", x4, "X5=", x5)
# print(linebreak)

# #Oppgave 2
# print("Oppgave 2")

# userInput = int(input("Enter an number: "))
# def factorial(userInput):
#     if userInput < 0 :
#         print("The number is negative")
#     elif userInput == 0 :
#         return 1 
#     else :
#         result = 1
#         for i in range (1, userInput+1) :
#             result *= i
#         return result
        
        
# result = factorial(userInput)
# print(result)
# print(linebreak)
    
    
# #Oppgave 3
# print("Oppgave 3")


# xInput = int(input("Enter x: "))
# yInput = int(input("Enter y: "))

# def integerPower(xInput, yInput) :
#     if yInput < 0 :
#         return "Not a valid number"
#     elif yInput == 0 :
#         return "Cant be zero"
#     else :
#         return xInput ** yInput
    
 
# result = integerPower(xInput, yInput)
# print(result)

# #Oppgave 4
# print("Oppgave 4")

# numberOne = int(input("Enter number one: "))
# numberTwo = int(input("Enter number Two: "))

# def multi(numberOne, numberTwo):
#     if numberTwo % numberOne :
#         return True
#     else :
#         return False

# result = multi(numberOne, numberTwo)
# print("The output is: ",result)
# print(linebreak)

#Oppgave 5
print("Oppgave 5")

def fahrenheit_to_celsius(temp):
    celsius = (5/9)*(temp-32)
    return celsius

def celsius_to_fahrenheit(temp):
    fahrenheit = (9/5)*temp + 32
    return fahrenheit

while True:
    print("Enter 1 for C to F\nEnter 2 for F to C\n" + linebreak)
    choice = int(input())

    if choice == 1:
        print("Enter temperature in Celsius:")
        celsius = float(input())
        fahrenheit = celsius_to_fahrenheit(celsius)
        print("{:.2f} Celsius = {:.2f} Fahrenheit".format(celsius, fahrenheit))
    elif choice == 2:
        print("Enter temperature in Fahrenheit:")
        fahrenheit = float(input())
        celsius = fahrenheit_to_celsius(fahrenheit)
        print("{:.2f} Fahrenheit = {:.2f} Celsius".format(fahrenheit, celsius))
    else:
        print("STOP!")
        break
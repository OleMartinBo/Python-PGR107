lineBreak = "-"*20 + "\n"

#Oppgave 1

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
# x3 = k(g (2) + h(2))
# x4 = f(0) + f(1) + f(2)
# x5 = f(-1) + g(-1) + h(-1) + k(-1)

# print("x1 =", x1, "x2 =", x2, "x3 =", x3, "x4 =", x4, "x5 =", x5)
# print(lineBreak)

# #Oppgave 2 

# def factorial(n):
       
#     if n == 0:
#         return 1
      
#     return n * factorial(n-1)
   
# number = int(input("Write a number: "))
# if number < 0:
#     print("Write only positive numbers.")
# else:
#     fact = factorial(number)
#     print(f"factorial of {number} is {fact}")

# print(lineBreak)

# #Oppgave 3

# x = int(input("Enter value of x: "))
# y = int(input("Enter value of y (positive & nonzero): "))

# def integerPower(x, y):
#     result = pow(x, y)
#     if y > 0:
#        return result 
#     else:
#         print(f"{y} is not positive. Write an positive & nonzero integer")

# result = integerPower(x, y)
# print(f"{x} that raised with the integer {y} is {result}")


# print(lineBreak)

# #Oppgave 4

# def multiple(i1, i2):
#     if i2 % i1 == 0:
#         return f"{i2} is a multiple of {i1}"
#     else:
#         return f"{i2} is not multiple of {i1}"

# integer1 = int(input("Enter first number: "))
# integer2 = int(input("Enter second number: "))

# result = multiple(integer1, integer2)
# print(result)

#Oppgave 5

#funksjon konverterer farenheit / celsius

def fahrenheit_to_celsius(F):
    return (5/9)*(F-32)

def celsius_to_fahrenheit(C):
    return (9/5)*C + 32

#Funksjon meny 
def menu():
    print("-"*45)
    print("Hello! welcome to the temperature converter!")
    print("Enter 1 to convert from Celsius to Fahrenheit")
    print("Enter 2 to convert from Fahrenheit to Celsius")
    print("-"*45)
  
#valg
while True:
    menu()
    userInput = int(input("Select 1 or 2: "))

    if userInput == 1:
        celsius = float(input("Enter temperature in Celsius to get it in farenhet: "))
        farenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius are {farenheit} Fahrenheit")
    elif userInput == 2:
        farenheit = float(input("Enter temperature in Fahrenheit to get it in celsius: "))
        celsius = fahrenheit_to_celsius(farenheit)
        print(f"{farenheit} Fahrenheit are {celsius} Celsius")
    else:
        print("STOP! Enter valid number >:( !")
        break




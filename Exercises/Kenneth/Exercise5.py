from math import sqrt

space = "------------"

print("Oppgave 1 \n" + space)

def f (x):
    return g (x) + sqrt (h(x))
    # TAKES AN INPUT VALUE X AND RETURNS A SUM OF TWO EXPRESSIONS
    # THE OUTPUT OF ANOTHER FUNCTION g(x) 
    # AND THE SQURE ROOT OF THE OUTPUT OF A THIRD FUNCTION h(x)
def g (x):
    return 4  * h(x)
    # THE FUNCTION g(x) TAKES INPUT x AND RETURNS THE OUTPUT OF AN ANTOHER FUNCTION
    # h(x) MULTIPLIED BY 4. 

def h (x):
    return x * x + k(x)-1
    #THE FUNCTION h(x) TAKES AN INPUT VALUE x  AND RETURNS THE RESULT
    #OF AN MATHEMATICAL EXPRESSION INVOLVING TWO FUNCTIONS 
    # k(x) and x 
def k (x):
    return 2 * (x+1)
    #FUNCTION k(x) TAKES INPUT x AND RETURN THE RESULT OF AN MATHEMSTICAL EXPRESSION 
    #INVOLVING x AND THE CONSTANT 1 

print("a \n" )

x1 = f (2) 
print(x1)
print(space)

print("b \n" )

x2 = g (h (2)) 
print(x2)
print(space)

print("c \n" )

x3 = k (g (2) + h (2)) 
print(x3)
print(space)

print("d \n" )


x4 = f(0) + f(1) + f(2)
print(x4)
print(space)

print("e \n")

x5 = f (-1) + g (-1) + h (-1) + k (-1) 
print(x5)
print(space)


print("Oppgave 2 \n" + space)

def factorial(n):
    if n < 0:
      return None
    elif n == 0: 
        return 1 
    else:
        result = 1 
        for i in range(1, n+1):
            result *= i
        return result

print(factorial(6))
print(factorial(0))
print(factorial(-6))

print(space)

print("oppgave 3")




def integerPower(x, y):  
    result = 1 
    for i in range(y): 
        result *=x 
    return result 

    




x = int(input("Enter a value for X: "))
y = int(input("Enter a value for Y: "))
result = integerPower(x, y)
print (f"{x} raised to the power of {y} is {result}")

print("Oppgave 5 \n" +space)

def multiple(a, b): 
    if b % a ==0:
        return f"{b} is a multiple of {a}"
    else: 
        return f"{b} is not a multiple of {a}"

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

result = multiple(a,b)

print(result)




def fahrenheit_to_celsius(fahrenheit): 
    return (5/9) * (fahrenheit -32)

def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius +32

while True:
    print("Enter 1 to convert from Celsius to Fahrenheit: ")
    print("Enter 2 to convert from Fahrenheit to Celsius: ")
    print("Select 1 or 2: ")

    choice = int(input())
    if choice == 1: 
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print("{:.2f} Celsius = {:.2f} Fahrenheit".format(celsius, fahrenheit))
    elif choice == 2: 
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print("{: .2f} Fahrenheit = {: .2f} Celsius".format(fahrenheit,celsius))
    else:
        print("STOP!")
        break 

    


    


from math import sqrt

#Oppgave 1. What do these code fragments print?

space = "----------"

print("Oppgave 1: ")
print("Oppg A \n" + space)
n=1
m=1

if n<-m : 
    print(n)
else : 
    print(m)

print(space)

print("Oppg B \n" + space)

n=1
m=-1
if -n > m : 
    print(n)
else : 
    print(m)
print(space)

print("Oppg C \n" + space)

x= 0.0
y= 1.0
if abs(x-y) < 1 : 
    print(x)
else :
    print(y)
print(space)

print("Oppg D \n" + space)

x= sqrt(2.0)
y=2.0
if x * x == y : 
    print(x)
else : 
    print(y)

#oppgave 2. 
"""
print("Oppgave 2: ")

userInput = int(input("Enter a number between 1 and 10: "))

if userInput > 10 : 
    print(" The number you entered is > 10")
elif userInput < 1 : 
    print("The number u entered is < 1")

elif userInput == 5 : 
    print("The number u entered is 5")

else : 
    print("The number you entered is: " + str(userInput))

"""

#oppgave 3. 
print("Oppgave 3: ")

gradeInput = int(input("Enter the score (0-100): "))

if gradeInput > 100 : 
    print(" the input is invalid. The score must be in the rage (0-100)")
elif gradeInput >89 : 
    print(" your grade is A")
elif gradeInput > 79 : 
    print("your grade is B")
elif gradeInput > 69 : 
    print("Your grade is C")
elif gradeInput >60 : 
    print("Your grade is D")
else : 
    print("Your grade is F ")

print(space)

#Oppgave 4.
print("Oppgave 4: ")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == '+':
    result = a + b
    print(f"{a} + {b} = {result}")
elif operator == '-':
    result = a - b
    print(f"{a} - {b} = {result}")
elif operator == '*':
    result = a * b
    print(f"{a} * {b} = {result}")
elif operator == '/':
    if b != 0:
        result = a / b
        print(f"{a} / {b} = {result}")
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operator or operator is not in the list.")
print(space)

#Oppgave 5. 
print("Oppgave 5: ")
weight = float(input("Enter weight: "))
unit = input("Enter the unit of weight (kg or lbs): ")

if unit == 'kg':
    pounds = weight * 2.2
    print(f"{weight} kg = you are {pounds}  lbs")
elif unit == 'lbs':
    kilograms = weight * 0.45
    print(f"{weight} lbs = you are {kilograms} kg")
else:
    print("Invalid unit.")

#Oppgave 6
print("Oppgave 6: ")

string = input("Enter a string: ")

if string.isalpha() :
    print("Contains only letters.")
else:
    print("Doesnt contain only letters")

if string.isupper():
    print("Contains only uppercase letters.")
else:
    print("Doesnt contain uppercase")

if string.islower():
    print("Contains only lowercase letters.")
else: 
    print("Doesnt contain lowercase")
  
if string.isdigit():
    print("Contains only digits.")
else: 
    print("Doesnt Contains only digits")
  
if string.isalnum():
    print("Contains only letters and digits.")
else: 
    print("Doesnt contain only letters and digits")

if string.endswith("."):
    print("Contains .")
else:
    print("Doesnt contain .")

if string[0].isupper() :
    print("Start with uppercase")
else:
    print("Doesnt start with uppercase")


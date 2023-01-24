from math import sqrt

linebreak = "----------------"
#Oppgave 1
print("Oppgave 1: ")
print(linebreak)

#A
n = 1
m = -1
if n < -m :
    print(n)
else :
    print(m)
    
print(linebreak)

#B
if -n >= m :
  print(n)
else:
  print(m)
  
print(linebreak) 

#C
x = 0.0
y = 1.0
if abs(x -y) < 1:
  print(x)
else:
  print(y)

print(linebreak)

#D
x = sqrt(2.0)
y = 2.0
if x * y == y :
  print(x)
else:
  print(y)
  
print(linebreak)
print(" ")

#Oppgave 2
print("Oppgave 2: ")
print(linebreak)

# userInput = int(input("Enter a number between 1 and 10: "))

# if userInput > 10 :
#     print(linebreak)
#     print("The number you entered is > 10")
# elif userInput < 1 :
#     print(linebreak)
#     print("The number you entered is < 1")
# else:
#     print(linebreak)
#     print("The number you entered is: " + str(userInput))
    
print(linebreak)
print(" ")

#Oppgave 3 
print("Oppgave 3:")
gradeInput = int(input("Enter the score (0-100): "))

if gradeInput > 100 :
    print(linebreak)
    print("Invalid input. The score must be in the range (0-100)")
elif gradeInput > 89 :
    print(linebreak)
    print("The letter grade is A!")
elif gradeInput > 79 :
    print(linebreak)
    print("The letter grade is B!")
elif gradeInput > 69 :
    print(linebreak)
    print("The letter grade is C!")
elif gradeInput > 60 :
    print(linebreak)
    print("The letter grade is D!")
elif gradeInput < 0 :
    print(linebreak)
    print("Invalid input. The score must be in the range (0-100)")
else:
    print(linebreak)
    print("The letter grade is F! You got: " + str(gradeInput) + "/100 score")
    
print(linebreak)
print(" ")

#Oppgave 4
print("Oppgave 4: ")
aNumber = float(input("Enter a: "))
bNumber = float(input("Enter b: "))
operatoType = input("Enter operator type: ")

if operatoType == "*" :
    result = aNumber * bNumber
    print("Result is: ", result)
elif operatoType == "/" :
    if bNumber != 0 :
        result = aNumber / bNumber
        print("Result is: ", result)
    else :
        print("Invalid, cant divide by 0")
elif operatoType == "+" :
    result = aNumber + bNumber
    print("Result is: ", result)
elif operatoType == "-" :
    result = aNumber - bNumber
    print("Result is: ", result) 
else :
    print("Not a valid operator!")
    
print(linebreak)
print(" ")

#Oppgave 5
print("Oppgave 5: ")
converterNumber = 2.2046226218
weightInput = float(input("Weight: "))
converterInput = str(input("(L)bs or (K)g: "))


if converterInput == "L" :
    if weightInput != 0 :
        result = weightInput / converterNumber
        print("You are ", result, " Kg(s)")
    else :
        print("Cant devide by 0")
elif converterInput == "K" :
    result = weightInput * converterNumber
    print("You are ", result, " Lb(s)")
else :
  print("Not av valid Statment")
  
print(linebreak)
print(" ")

#Oppgave 6
print("Oppgave 6: ")

    

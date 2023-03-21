
############################
#       EXCERCISE 1
#   NUMBERS AND STRINGS
############################

""" 
#task 4:Write a program that prompts the user for two integers and then prints
a. The sum
b. The difference
c. The product
d. The average
e. The distance (absolute value of the difference)
f. The maximum
g. The minimum

n1 = int(input("Enter integer 1: "))
n2 = int(input("Enter integer 2: "))

print("sum", n1 +n2)
print("difference", n1 -n2)
print("Product", n1*n2)
print("The average: ", (n1+n2)/2)
print("The distance:", abs(n1-n2))
print("the min", max(n1, n2))
print("the max", min(n1, n2) )


#5. Properly format the outputs in Exercise 4 as follows.

n1 = int(input("Enter integer 1: "))
n2 = int(input("Enter integer 2: "))
print("\n")
print("%-15s" % "sum", n1 +n2)
print("%-15s" % "difference", n1 -n2)
print("%-15s" % "Product", n1*n2)
print("%-15s" % "The average: ", (n1+n2)/2)
print("%-15s" % "The distance:", abs(n1-n2))
print("%-15s" % "the min", max(n1, n2))
print("%-15s" % "the max", min(n1, n2) )


6. Write a program that asks the user for the lengths of the sides of a 
rectangle. Then print the area and perimeter of the rectangle.


s1 = int(input("Enter side 1: "))
s2 = int(input("Enter side 1: "))

area = s1 * s2
perimeter = (s1 * s2)*2

print("The area of the rectangle: ", area)
print("The perimeter of the rectangle: ", perimeter)


7. Write a program that initializes a string variable and prints the first two 
characters, followed by three periods, and then the last two characters.
For example, if the string is initialized to "Mississippi", then print Mi...pi.

word = "Mississippi"

length = len(word)

print(word[0] + word[1] + "..." + word[length-2] + word[length-1])


8. Write a program that reads a five-digit positive integer and breaks it into a 
sequence of individual digits. For example, the input 16384 is displayed as
1 6 3 8 4


digits = input("enter five positive digits: ")
print(digits[0], digits[1], digits[2], digits[3], digits[4])

############################
#       EXCERCISE 2
#        DECISIONS
############################

2. Write a program that uses an if/elif/else sequence to validate the user’s input to be in the range 1-10. The number is entered by the user and the program will determine if 
the number is between 1 and 10. If the number entered is less than 1, the program will print “The number you entered is < 1”. If the number entered is greater than 10, 
the program will print “The number you entered is > 10”. If the number is between 1 and 10, the program will print the number.

number = int(input("Enter a number between 1-10: "))

if number <= 0:
    print("The number you enteres is <1")
elif number >10:
    print("the number is >10")
else:
    print("The number you enteres is: ", number)

3. Write a program that assigns letter grade for a quiz according to the following table and 
then prints the letter grade. Print a message if the input is not valid.


score = int(input("enter score 0-100: "))

if score > 100:
    print("invalid number.")
elif score >= 90:
    print("The letter grade is A")
elif score >= 80:
    print("the letter grade is B")
elif score >= 70:
    print("The letter grade is C")
elif score < 0:
    print("invalid number")
else:
    print("the letter grade is F")


4. Write a program that calculates multiplication, division, addition or subtraction of two numbers,
a and b, entered by the user. The user will also enter operator type (*, /, + or -). If the operator is (*), the program will compute (a*b). 
If the operator is (/), the program will compute (a/b) (if b is not equal to zero). If the operator is (+), the program will compute (a+b). And if the operator is (-), the program will compute a-b. For any other operators, the program prints the message: “Invalid operator or operator is not in the list”.
Sample

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
operator = input("Enter operator type *, / + or - :")

if operator == "*":
    print(a * b)
elif operator == "/":
    if b == 0:
        print("b cant be 0")
    else:
        print(a / b)
elif operator == "+":
    print(a + b)
elif operator == "-":
    print(a-b)
else:
    print("the operator is not in the list")


5. Write a program to get a weight in either Pound (lbs) or Kilogram (kg) and converts it to the other unit.
1 Kilogram = 2.2 Pounds and 1 Pound = 0.45 Kilogram.


weight = float(input("enter weight: "))
type = input("P for pound or K for KG: ")

if type == "P":
    kg = weight * 0.45
    print(f"you are {kg} kilos")
elif type == "K":
    pound = weight * 2.2
    print(f"You are {pound} pounds")
else:
    print("invalid input")


6. Write a program that reads in a string and prints whether it
• contains only letters.
• contains only uppercase letters.
• contains only lowercase letters.
• contains only digits.
• contains only letters and digits.
• starts with an uppercase letter.
• ends with a period.

s = input("Enter a string: ")

if s.isalpha():
    print("the string contains only letters")
else:
    print("the string contains not anly letters")

if s.isupper():
    print("the string contaons only uppercase letter")
else:
    print("the string does not contain only uppercase letter")

if s.isdigit():
    print("the strirng contains only digits")
else:
    print("the string does not contain only digits")

if s.isalnum():
    print("The string contains letters AND digits")
else:
    print("the string does not contain letter and digits")

if s[0].isupper():
    print("the first letter is uppercase")
else:
    print("the first litter is not uppercase")

if s.endswith("."):
    print("the string ends with period ")
else:
    print("the string does not end with period ")

    
############################
#       EXCERCISE 3
#       WHILE LOOP
############################


task 2. Using a while loop, write a program to print all squares less
than n (which is entered by the user). For example, if n is 100, print 0 1 4 9 16 25 36 49 64 81.


n = int(input("Enter n: "))
i = 0

print(f"all squares less than {n}: ")
while i**2 < n:
    print(i ** 2, end=" ")
    i = i + 1

3. Write a program, using while loop, that prints a Celsius/Fahrenheit 
conversion table such as the following using the formula: C * (9/5) + 32 = F


celsius = 0
print("| Cellsius  | Farenheit |")
print("------------+------------")

while celsius <= 100:
    fahrenheit = celsius * (9/5) + 32
    print("%11d | %10d" % (celsius, fahrenheit))
    celsius += 10  #intervall på 10 opp til 100

task 4. Write a program that reads a student record, consisting of the student’s first and last name, followed by a sequence of test scores 
and a sentinel of –1. The program should print the student’s average score.


fname = input("Enter your first name: ")
lname = input("Enter ypur last name: ")

total = 0
count = 0

score = int(input("Enter score or 1 to exit: "))

while score != 1:
    if score < 0 or score > 100:
        print("Invalid score!")
    else:
        total = total + score
        count += 1
    score = int(input("Enter score or 1 to exit: "))
if count != 0:
    avg = total / count
    print("Student name: ", fname, lname)
    print("The avg score: %.2d" % avg)
else:
    print("No valid score entered.")

    
Write programs that read a line of input as a string and print
a. Only the uppercase letters in the string.

string = input("Enter a string: ")

def uppercase():
    i = 0
    while i < len(string):
        if string[i].isupper():
            print(string[i], end="")
        i = i + 1 
#uppercase()

b. Every second letter of the string.

def secondLetter():
    i = 0

    while i < len(string):
        print(string[i])
        i = i + 2
#secondLetter()

c. The string, with all vowels replaced by an underscore.

def vowelUnderscore():
    i = 0
    vowel = "aeiouAEIOU"

    while i < len(string):
        if string[i] in vowel:
            print("_", end="")
        else:
            print(string[i], end="")
        
        i = i + 1

#vowelUnderscore()

d. The number of digits in the string.

def digits():
    i = 0
    digits = 0

    while i < len(string):
        if string[i].isdigit():
            digits += 1
        i = i + 1
    print(f"There are {digits} digits in the string")

#digits()

e. The positions of all vowels in the string.

def positionVowels():
    i = 0
    vowel = "aeiouAEIOU"
    v = False
    while i < len(string):
        if string[i] in vowel:
            print(i, end="")
            v = True
        i += 1
    if not v:
        print("No vowel in input")


positionVowels()

6. Write a program that reads a set of floating-point values. Ask the user to enter the values, then print
• the average of the values.
• the smallest of the values.
• the largest of the values.
• the range, that is the difference between the smallest and largest.



#AVERAGE OF THE VALUES

def avg():

    total = 0
    count = 0

    inputString = input("Enter a floating point value or Q to exit: ")
    while inputString.upper() != "Q":
        value = float(inputString) #konverterer string til float
        total += value
        count += 1
        inputString = input("enter a floating point value or Q to exit: ")

    if count != 0:
        avg = total / count
        print("AVG = %.2f" % avg)
    else:
        print("no valid input entered")

#avg()


def smallestLargestRange():


    value = float(input("Enter a floating point number: "))
    largest = value
    smallest = value

    inputStr = input("Enter a float number or Q to exit: ")

    while inputStr.upper() != "Q":

        value = float(inputStr)
        if value > largest:
            largest = value
        elif value < smallest:
            smallest = value

        inputStr = input("Enter a floating point number, or Q to exit: ")
    
    range = smallest - largest

    print(f"\n Smallest= {smallest}, Largest= {largest}, range= {range}")


#smallestLargestRange()
    

#task 7. Write a program that reads a word and prints each character of the word on a separate line. For example,
if the user provides the input "Harry", the program prints


word = input("Enter a word: ")
i = 0

while i < len(word):
    print(word[i])
    i +=1


8. Write a program that reads a word and prints the word in reverse. For example, if the user provides the
input "Harry", the program prints


#Smallest, largest and range 
# > større enn 
# >= større eller lik
# < mindre enn
# <= mindre eller lik 



word = input("Enter a word: ")
index = len(word) - 1

while index >= 0:
    print(word[index], end="")
    index -= 1


############################
#       EXCERCISE 4
#       FOR LOOP
############################

Task 2. Write programs using for loop that read a line of input as a string and print:

userInput = input("Enter a string: ")

# a. Only the uppercase letters in the string.

for char in userInput:
    if char.isupper():
        print(char, end="")

print("\n")

# b. Every second letter of the string.

for i in range(0, len(userInput), 2):
    print(userInput[i], end="")

print("\n")

# c. The string, with all vowels replaced by an underscore.

for char in userInput:
    if char in "aAeEiIoOuU":
        print("_", end="")    
    else:
        print(char, end="")
print("\n")

# d. The number of digits in the string.
digits = 0

for char in userInput:
    if char.isdigit():
        digits += 1

print("Number of digits = ", digits)
print("\n")

# e. The number of vowels in the string.

vowels = 0

for char in userInput:
    if char in "aAeEiIoOuU":
        vowels += 1

print("Number of vowels= ", vowels)
print("\n")



#Task 3. Write a program using for loop that reads a word and prints each character of 
# the word on a separate line. For example, if the user provides the input "Harry", the program prints

word = input("Enter a word: ")

for char in word:
    print(char)


#Task 4. Write a program using for loop that reads a word and prints the word in reverse. 
For example, if the user provides the input "Harry", the program prints

word = input("Enter a word: ")
revWord = ""

for char in word:
    revWord = char + revWord
print(revWord)


task 5. Write a program using nested for loop to produce the following shape.

row = int(input("Enter row number: "))

for i in range(row):
    for j in range(i+1):
        print("*", end="")
    print()

6. Write a program using nested for loop to draw the following shapes.
XXXXX
XX
XXXXX
XX
XX

XX
XX
XX
XX
XXXXX


ROW = 5

for i in range(ROW):
    if i == 0 or i == 2:
        print("X" * 5)
    else:
        print("X" * 2)

print("\n")

ROW = 5

for i in range(ROW):
    if i == 4:
        print("X" * 5)
    else:
        print("X" * 2)

        
############################
#       EXCERCISE 5
#       FUNCTIONS
############################

"""
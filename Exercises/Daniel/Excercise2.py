from math import sqrt
import sys


#n = 1
#m = -1
#if n < -m:
#    print(n)
#else:
#    print(m)

#if -n >= m:
    #print(n)
#else:
    #print(m)
    
#x = 0.0
#y = 1.0

#if abs(x-y) < 1:
 #   print(x)
#else:
 #   print(y)
 
#x = sqrt(2.0)
#y = 2.0
 
#if x * x == y:
#    print(x)
#else:
#    print(y)

#userInput = int(input("Enter a number between 1 and 10: "))

#if userInput < 1:
#    print("You entered a number < 1")
#elif userInput > 10:
#    print("The number you entered is > 10")
#else:
#    print(userInput)

# userInput = input("Enter your grade number: ")

# if userInput.isdigit():
#     userInput = int(userInput)

#     if userInput < 1 or userInput > 100:
#         print("Please type a number larger than 1, and lower than 100.")
#         sys.exit()
# else:
#         print("Please type a number next time.")
#         sys.exit()

# if userInput >= 90 and userInput <= 100:
#     print("Your lettergrade is: A")
# elif userInput >= 80:
#     print("Your lettergrade is: B")
# elif userInput >= 70:
#     print("Your lettergrade is: C")
# elif userInput >= 60:
#     print("Your lettergrade is: D")
# elif userInput < 60:
#     print("Your lettergrade is: F")

# a = input("Type a number: ")
# b = input("Type a number: ")

# operator = input("Enter operator: ")

# if operator == "+":
#     result = a + b
#     print("Your result is: %d" % result)
# elif operator == "-":
#     result = a - b
#     print("Your result is: %d" % result)
# elif operator == "*":
#     result = a * b
#     print("Your result is: %d" % result)
# elif operator == "/":
#     result = a / b
#     print("Your result is: %d" % result)
# else:
#     print("Your input is wrong")

# print("Welcome to the weight converter!\n")
# weight = int(input("Enter a weight in a whole number: "))
# converter = input("\nPress l if you entered the weight in pounds. Press k for kilograms: ")

# if converter == "l":
#     weight = weight * 0.45
#     print("The weight is: %d Kilo(s)" % weight)
# else:
#     weight = weight * 2.2
#     print("The weight is: %d Pounds" % weight)

# Write a program that reads in a string and prints whether it 
# • contains only letters. 
# • contains only uppercase letters. 
# • contains only lowercase letters. 
# • contains only digits. 
# • contains only letters and digits. 
# • starts with an uppercase letter. 
# • ends with a period. 

sentence = input("Enter a sentence: ")

if sentence.isalpha():
    print("The sentence contains only letters")
else: 
    print("The sentence does not only have letters")
    
if sentence.isupper():
    print("The sentence contains only capital letters")
else: 
    print("The sentence does not only have capital letters")
    
if sentence.islower():
    print("The sentence contains only lowercase letters")
else: 
    print("The sentence does not only have lowercase letters")
    
if sentence.isdigit():
    print("The sentence contains only digits")
else: 
    print("The sentence does not only have digits")
    
if sentence.isalnum():
    print("The sentence contains letters and numbers")
else: 
    print("The sentence does not have both letters and numbers")
    
if sentence[0].isupper():
    print("The sentence starts with a capital letter")
else: 
    print("The sentence does not start with a capital letter")
    
if sentence.endswith("."):
    print("The sentence ends with a period")
else: 
    print("The sentence does end with a period")


        
    


    
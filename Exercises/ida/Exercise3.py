# #Task1

# print("_________________")
# print("     Task A      ")
# print("_________________ \n")
# lineBreak = "-----------------"
# i = 0
# j = 10
# n = 0
# while i < j :
#     i = i + 1
#     j = j - 1
#     n = n + 1 
#     print("%2s" % str(i), "%2s" % "|", "%2s" % str(j), "%2s" % "|", "%2s" % str(n), "%2s" % "|")
#     print(lineBreak)

# print("_________________")
# print("     Task B      ")
# print("_________________ \n")

# i = 0
# j = 0
# n = 0
# while i < 10 : 
#     i = i + 1
#     n = n + i + j
#     j = j + 1
#     print("%2s" % str(i), "%2s" % "|", "%2s" % str(j), "%2s" % "|", "%2s" % str(n), "%2s" % "|")
#     print(lineBreak)

# print("_________________")
# print("     Task C      ")
# print("_________________ \n")

# i = 10
# j = 0
# n = 0
# while i > 0 : 
#     i = i - 1
#     j = j + 1
#     n = n + i - j
#     print("%2s" % str(i), "%2s" % "|", "%2s" % str(j), "%2s" % "|", "%2s" % str(n), "%2s" % "|")
#     print(lineBreak)


# print("_________________")
# print("     Task D      ")
# print("_________________ \n")

# i = 0
# j = 10
# n = n + 1
# while i !=j :
#     print("%2s" % str(i), "%2s" % "|", "%2s" % str(j), "%2s" % "|", "%2s" % str(n), "%2s" % "|")
#     print(lineBreak)


# print("_________________")
# print("     Task 2      ")
# print("_________________ \n")

# n = int(input("Enter a number: "))
# i = 0
# while i**2 < n:
#     print(i**2, end=' ')
#     i += 1

# print("_________________")
# print("     Task 3      ")
# print("_________________ \n")

# c = 0
# f = 0 
# print("%s" % "|","%5s" % "Celsius", "%6s" % "|", "%7s" % "Fahrenheit", "%4s" % "|")
# print("--------------------------------")

# while c <= 100 : 
#     f = c * (9/5) * 32
#     print("%5s" % str(c), "%8s" % "|", "%5s" % str(f), "%5s" % "|")
#     c = c + 10


#4

# firstName = input("Write your first name: ")
# lastName = input("Write your last name: ")
# total = 0
# count = 0

# score = float(input("Enter score or -1 to exit: "))

# while score != -1:
#     if score < 0 or score > 100:
#         print("Invalid score!")
#     else:
#         total = total + score 
#         count = count + 1

#     score = float(input("Enter a score or -1 to exit: "))

# if count != 0:
#         avg = total / count
#         print("\n Student:", firstName, lastName)
#         print("The average score = %.2f" % avg)
# else:
#         print("No valid score entered.")

#5
# #Oppgave a 
# lineInput = input("Enter a line of input as a string: ")

# i = 0

# while i < len(lineInput):
#     if lineInput[i].isupper():
#      print(lineInput[i])
#     i = i + 1

# #Oppgave b

# lineInput = input("Enter a line of input as a string: ")

# i = 0 

# while i < len(lineInput):
#    print(lineInput[i])
#    i = i + 2

#Oppgave c 
# lineInput = input("Enter a line of input as a string: ")
# i = 0 
# while i < len(lineInput):
#     if lineInput[i].lower() in "aeiou" or lineInput.upper() in "AEIOU":
#       print("_", end="")
#     else:
#       print(lineInput[i], end="")
    
#     i = i + 1

#oppgave d

# lineInput = input("Enter a line of input as a string: ")
# i = 0
# digits = 0

# while i < len(lineInput):
#    if lineInput[i].isdigit():
#       digits += 1

#    i = i + 1
# print(f"In the string, there are {digits} digits")


#oppgave e

# lineInput = input("Enter a line of input as a string: ")
# i = 0
# vowel = False 
# while i < len(lineInput):
#     if lineInput[i].lower() in "aeiou" or lineInput.upper() in "AEIOU":
#         print(i, end=" ")
#         vowel = True 

#     i = i + 1

# if not vowel:
#     print("No vowels in the entered string")

#Oppgave 6

# total = 0
# count = 0
# largest = None
# smallest = None

# inputStr = input("Enter a floating-point number or E to Exit): ")

# while inputStr.upper() != "E":
#         value = float(inputStr)
#         total += value
#         count += 1
        
#         if largest is None or value > largest:
#             largest = value
        
#         if smallest is None or value < smallest:
#             smallest = value
        
#         inputStr = input("Enter a floating-point number or E to Exit): ")

# if count > 0:
#     avg = total / count
#     print("Average = %.2f" % avg)
# else:
#     print("No valid input entered.")
    
# if largest is not None and smallest is not None:
#     range = largest - smallest
#     print(f"Smallest = {smallest}, \n Largest = {largest}, \n Range = {range}")
# else:
#     print("No values entered.")


#Oppgave 7

print("------------")
print(" Task 7")
print("------------")


wordInput = input("Enter a word: ")
index = 0

while index < len(wordInput):
    print(wordInput[index])
    index += 1

print("------------")
print(" Task 8")
print("------------")

wordInput = input("Enter a word: ")
index = len(wordInput) - 1

while index >= 0:
    print(wordInput[index], end="")
    index -= 1



    

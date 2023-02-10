# #Oppgave 1
linebreak = "_" * 23

# #A
# i = 0
# j = 10
# n = 0
# print("Oppgave A")
# print(linebreak)
# while i < j :
#   i = i + 1
#   j = j - 1
#   n = n + 1
#   print("%3s" % str(i), "%3s" % "|" , "%3s" % str(j),"%3s" % "|","%3s" % str(n), "%3s" % "|")
#   print(linebreak)
  

# #B
# i = 0
# j = 0
# n = 0
# print("Oppgave B")
# print(linebreak)
# while i < 10:
#     i = i + 1
#     n = n + i + j
#     j = j + 1
#     print("%3s" % str(i), "%3s" % "|" , "%3s" % str(j),"%3s" % "|","%3s" % str(n), "%3s" % "|")
#     print(linebreak)
    
# #C
# i = 10
# j = 0
# n = 0
# print("Oppgave C")
# print(linebreak)
# while i > 0:
#     i = i - 1
#     n = j + 1
#     j = n + i -j
#     print("%3s" % str(i), "%3s" % "|" , "%3s" % str(j),"%3s" % "|","%3s" % str(n), "%3s" % "|")
#     print(linebreak)
    
# # #D
# # i = 0
# # j = 10
# # n = 0
# # print("Oppgave D")
# # print(linebreak)
# # while i != j:
# #     i = i + 2
# #     n = j - 2
# #     j = n + 1
# #     print("%3s" % str(i), "%3s" % "|" , "%3s" % str(j),"%3s" % "|","%3s" % str(n), "%3s" % "|")
# #     print(linebreak)
# print(linebreak)
# print(" ")


# # #Oppgave 2
# # print("Oppgave 2")
# # userInput = int(input("Enter a number: "))
# # print(linebreak)
# # square = 0

# # while square * square < userInput:
# #   square = square + 1
# #   print(square * square)

# # print(linebreak)
# # print(" ")

# #Oppgave 3
# print("Oppgave 3")

# c = 0
# f = 0
# maxGrense = int(input("Enter max: "))
# print(linebreak + "---------")
# print("%s" % "|","%5s" % "Celsius", "%6s" % "|", "%5s" % "Fahrenheit", "%4s" % "|")
# print(linebreak + "---------")

# while c <= maxGrense:
#     f = c * (9/5) + 32
#     print("%s" % "|", "%8s" % str(c), "%5s" % "|", "%10s" % str(f), "%4s" % "|")
#     print(linebreak + "---------")
#     c = c + 10


# #Oppgave 4
# print("Oppgave 4")
# fname = input("Enter your first name: ")
# lname = input("Enter your last name: ")
# total = 0
# count = 0
# score = float(input("Enter a score (-1 to exit): "))
# while score != -1:
#     if score < 0 or score > 100:
#         print("Invalid score!")
#     else:
#         total = total + score
#         count = count + 1
    
#     score = float(input("Enter a score (-1 to exit): "))
    
# if count != 0:                              ### Why do you need to check if count 
#     avg = total / count
#     print("\nStudent:",fname, lname)
#     print("The Average Score = %.2f" % avg)
# else:
#     print("No valid score entered.")
    
# #Oppgave 5
# print("Oppgave 5A")
# line = input("Enter a line of input: ")
# i = 0
# while i < len(line):
#     if line[i].isupper():
#         print(line[i])
    
#     i = i + 1
    
# print(linebreak)
# print("Oppgave 5B")

# line = input("Enter a line of input: ")
# i = 0
# while i < len(line):
#     print(line[i])
#     i = i + 2
    
# print(linebreak)
# print("Oppgave 5C")
# line = input("Enter a line of input: ")
# i = 0
# while i < len(line):             
#     if line[i].upper() in "AEIOU" or line[i].lower() in "aeiou":   
#         print("_", end="")
#     else:
#         print(line[i], end="")
        
#     i = i + 1

# print(linebreak)
# print("Oppgave 5D")
# line = input("Enter a line of input: ")
# i = 0
# digits = 0
# while i < len(line):
#     if line[i].isdigit():
#         digits += 1
        
#     i = i + 1
    
# print(f"There are {digits} digit(s) in the string.")

# print(linebreak)
# print("Oppgave 5E")
# line = input("Enter a line of input: ")
# i = 0
# vowel = False
# while i < len(line):
#     if line[i].upper() in "AEIOU" or line[i].lower() in "aeiou":
#         print(i, end=" ")
#         vowel = True
        
#     i = i + 1
# if not vowel:
#     print("No vowels in the input.")
    

# print(linebreak)
# print("Oppgave 6 Average")
# total = 0
# count = 0
# inputStr = input("Enter a floating-point number (Q to exit): ")
# while inputStr.upper() != "Q":
#     value = float(inputStr)
#     total = total + value
#     count = count + 1
#     inputStr = input("Enter a floating-point number (Q to exit): ")
    
# if count != 0:
#     avg = total / count
#     print("Average = %.2f" % avg)
# else:
#     print("No valid input entered.")
    
# print(linebreak)
# print("Oppgave 6 smallest, largest, and range")
# value = float(input("Enter a floating-point number: "))
# largest = value
# smallest = value

# inputStr = input("Enter a floating-point number (Q to exit): ")

# while inputStr.upper() != "Q":    
#     value = float(inputStr)      
#     if value > largest:
#         largest = value
        
#     if value < smallest:
#         smallest = value
        
#     inputStr = input("Enter a floating-point number (Q to exit): ")
    
# print("\nSmallest =", smallest)
# print("Largest =", largest)
# range_diff = largest - smallest
# print(f"The range (the difference between the smallest and largest) is {range_diff}")

print(linebreak)
print("Oppgave 7")
name = "Harray"
i = 0
while i < len(name) :
    letter = name[i]
    print(letter, end="")
    i = i + 1
    
print(linebreak)
print("Oppgave 8")
name = "Harray"
i = len(name) -1
while i >= 0 :
    print(name[i], end="")
    i = i - 1
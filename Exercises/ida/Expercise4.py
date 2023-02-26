
taskDone = "\n End of task \n"
lineBreak = "-" * 20

#Oppgave 1 

for rows in range(1, 10) :
    print(rows, end="")

for rows in range(1,10,2):
    print(rows, end="")

for rows in range(10, 1, -1):
    print(rows, end="")

for rows in range(10):
    print(rows, end="")

for rows in range(1,10): 
   if rows % 2 == 0:
       print(rows, end="")

print(taskDone, lineBreak)

#Oppgave 2 


inputLine = input("Enter a line of input: ")

#Print only uppercase letter in string 

for char in inputLine:
    if char.isupper():
        print(char, end="")

print(" ")
#Print second letter of string

for index in range(0, len(inputLine), 2):
    print(inputLine[index], end="")

print(" ")

#replace all vowels in the string with underscore
 

vowels = "aeiouAEIOU"
new_string = ""

for char in inputLine: 
    if char in vowels:
        new_string += "_"
    else:
        new_string += char
print(new_string, end="")

print(" ")

#Number of digits

digits = 0
for char in inputLine:
    if char.isdigit():
        digits += 1

print("number of digits in input: ", digits)


#number of vowels in string

letterVowels = "aeiouAEUOU"
vowels = 0
for char in inputLine:
    if char in letterVowels:
        vowels += 1
print("number of vowels in input: ", vowels)

print(taskDone, lineBreak)

#Oppgave 3

#Reads input in separat line with for-loop

wordInput = input("Enter a word: ")
for char in wordInput:
    print(char)

print(taskDone, lineBreak)

#Oppgave 4

wordInput = input("Enter a word: ")

wordReverse = ""
for char in wordInput:
    wordReverse = char + wordReverse

print(wordReverse)

print(taskDone, lineBreak)

#Oppgave 5 - NESTED FOR-LOOP

row = 5
for rows in range(row):
    for iterations in range(rows+1):
        print("*", end="")
    print()

print(taskDone, lineBreak)

#Oppgave 6 - NESTED FOR-LOOP

for rows in range(5):
    if rows % 2 == 0:  #ser om linjen er even eller odd 
        print("X"*5)
    else:
        print("XX")
print()
for rows in range(5):
    if rows == 4:
        print("X"*5)
    else:
        print("XX")
        

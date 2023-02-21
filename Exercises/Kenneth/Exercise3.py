
#1. Provide trace tables for these loops.
space = "------------"
print("1.a \n" + space)

i=0
j=10
n=0

print("i", "j", "n")
print("-", "-", "-")

while i < j : 
    print(i,j,n)
    i = i + 1
    j = j - 1
    n = n + 1
print(space)

print("1.b \n" + space)

print("i", "j", "n")
print("-", "-", "-")

i=0
j=0
n=0

while i < 10 : 
    print(i,j,n)
    i=i +1
    n=n + i +j 
    j=j + 1
print(space)

print("1.c \n" + space)
print("i", "j", "n")
print("-", "-", "-")
i=10
j=0
n=0
while i > 0 :
    print(i,j,n)
    i=i -1
    j=j +1
    n=n+i-j
print(space)

"""
print("1.d \n" + space)
print("i", "j", "n")
print("-", "-", "-")


i=0
j=10
n=0
while i != j : 
    print(i,j,n)
    i=1 +2
    j=j -2
    n=n +1
"""

#oppgave 2.
""" 
print("oppgave 2 \n" + space)

n = int(input("Enter a positive integer n: "))

i = 0
while i * i < n:
    print(i * i, end=" ")
    i = i + 1
print(space)
"""

#Oppgave 3
print("oppgave 3 \n" + space)
print("Celsius to Fahrenheit Conversion Table")
print("\n")
print("Celsius   Fahrenheit")
print("--------  -----------")

celsius = 0
while celsius <= 100:
    fahrenheit = celsius * (9/5) + 32
    print("{:>7.0f}    {:>7.0f}".format(celsius, fahrenheit))
    celsius = celsius + 10
"""
#oppgave 4
print("Oppgave 4 \n" + space)

fName= input("Enter first name: ")
lName= input("Enter last name: ")

sum= 0
count= 0
score = 0
print("Enter the student's test scores (Enter -1 to stop): ")

while score != -1: 
    score = float(input())
    if score != -1:
        sum += score
        count += 1

if count == 0: 
    print("No scores entered for student")
else:
    averageScore = sum / count
    print((f"{fName} {lName}´s avarage score is {averageScore: .2f}"))
"""
#oppgave 5 
"""
print("Oppgave 5a \n" + space)

string = input("Enter a line of input: ")
i=0
while i < len(string): 
    if string[i].isupper(): 
        print(string[i])
        i = i +1


    
print("Oppgave 5b \n" + space)  

string = input("Enter a line of input: ")

i=0
while i < len(string): 
    print(string[i])
    i = i + 2
"""
"""
print("Oppgave 5c \n" + space)  

string = input("Enter a line of text: ")
vowels ="aeiouyAEIOU"
outputString = ""
i=0

while i < len(vowels):
    string = string.replace(vowels[i], "_")
    
    i += 1

print(string)
"""
"""
while i < len(string): 
    if string[i] in vowels:
      print("string replaced with vowels", end="")
      i=i+1
 
 """     
""" 
print("Oppgave 5d \n" + space)

string = input("Enter a string: ")

count = 0

i=0
string_lenght = len(string)

while i < string_lenght: 
    char = string[i]
    if char.isdigit(): 
        count +=1
    i += 1    
print("The number if digits in the string is: " , count)

 """ 
""" 
print("Oppgave 5e \n" + space)

string = input("Enter a string: ")

vowel_position = []

i = 0

string_lenght = len(string)

while i < string_lenght:
    char = string[i]
    if char in "aeiouAEIOU":
        vowel_position.append(i)
    i += 1
    print("The position of vowels in string are: ", vowel_position)
 """ 


"""
print("Oppgave 6.1 \n" + space)


string = input("Enter the set of floating-point values sapareted by space: ")

values = [float(val) for val in string.split()]

average = sum(values) / len(values)

print("The average of the values is: ", average)
"""
"""
print("Oppgave 6.2 \n" + space)

string = input("Enter a set of floating-point values sapareted by space: ")
values = [float(val) for val in string.split()]

average = sum(values) / len(values)
smallest = min(values)
largest = max(values)
values_range = largest-smallest

print("The average of the values is: ", average)
print("The smallest value is: ", smallest)
print("The largest value is: ", largest)
print("The range of the values is ", values_range)
"""

print("Oppgave 7 \n" + space)

word = input("Enter a word: ")

i=0 
while i < len(word):
    print(word[i])
    i+=1

print("Oppgave 8 \n" + space)

word = input("Enter a word: ")
reverse_word = ""
i=len(word) -1

while i >=0:
    reverse_word +=word[i]
    i -=1

print("Reverse of the word is: ", reverse_word)    

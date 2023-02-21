
space = "------------"
"""
print("1.a \n" + space)
for i in range(1,10):
    print(i)

print(space)

print("1.b \n" + space)

for i in range(1,10,2):
    print(i)

print(space)

print("1.c \n" + space)
for i in range(10,1,-1):
    print(i)


print(space)

print("1.d \n" + space)

for i in range(10):
    print(10)

print(space)

print("1.e \n" + space)


for i in range(1,10):
    if i % 2 == 0:
        print(i)
"""
print(space)

"""
print("oppgave 2.a \n" + space)

string = input("Enter a string: ")

for char in string:
    if char.isupper(): 
        print(char)

print(space)

print("oppgave 2.b \n" + space)

string = input("Enter a string: ")
for i in range(0,len(string),2): 
    print(string[i])

print(space)
"""
"""
print("oppgave 2.c \n" + space)

string = input("Enter a string: ")
vowels = ['a','e','i','o','u']

newString = ""
for char in string: 
    if char.lower() in vowels:
        newString += "_"
    else:
        newString += char
print(newString)

print("oppgave 2.d \n" + space)

string= input("Enter a String: ")

count = 0

for char in string: 
    if char.isdigit():
        count += 1

print("Number of digits i the string: ", count)

print("oppgave 2.e \n" + space)

string = input("Enter a string: ")

vowels = ['a','e','i','o','u']

count = 0

for char in string:
    if char.lower() in vowels:
        count += 1
print(" Number of vowels in the string: ", count)
"""
"""
print("oppgave 3 \n" + space)

word = input("Enter a word: ")

for char in word:
    print(char)

print("oppgave 4 \n" + space)

word = input("Enter a word: ")

reverseWord= ""

for i in range(len(word) -1,-1,-1): 
    reverseWord += word[i]

print(" The word in reverse is: ", reverseWord)



print("oppgave 5 \n" + space)

for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()
print(space)

"""
print("oppgave 6.a \n" + space)

"""
row = 5 

for i in range(row): 
    if i == 0 or i == 2: 
        print("X"* 5)
    else:
        print("X"*2)
"""

row = 5
col = 5

for i in range(row):
    for j in range(col):
        if j == 0 or j == 1 or i == 0 or i ==2:
           print("X", end="")
        else: 
            print(end=" ")
    print()

print("\n")


"""
row = 5 

for i in range(row):
    if i == row -1:
        print("X" *5)
    else:
        print("X"*2)
"""

row = 5 
col = 5 

for i in range(row):
    for j in range (col): 
        if j == 0 or j == 1 or i == row -1:
            print("X", end="")
        else: 
            print(end="")
    print()

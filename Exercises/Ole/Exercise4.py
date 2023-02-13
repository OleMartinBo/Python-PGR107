linebreak = "-" * 20
space = " "

#Oppgave 1
print("Oppgave 1")
print(linebreak + space)

for i in range(1, 10) :
    print(i, " ", end="")
print()

print(linebreak + space)

for i in range(1, 10 , 2) :
    print(i, " " , end=" ")
print()

print(linebreak + space)

for i in range(10) :
    print(i, " ", end="")
print()

print(linebreak + space)

for i in range(1, 10) :
    if i %  2 == 0 :
        print(i, " ", end="")
print()

print(linebreak, space)

#Oppgave 2
# print("Oppgave 2")
# print(linebreak, space)

# userInput = input("Opp A: Enter a Uppercase string: ")
# uppsercase = ""

# for i in userInput :
#     if i.isupper() :
#         uppsercase += i
# print(uppsercase)

# print(linebreak, space)

# userInput = input("Opp B: Enter a string and every second will show: ")
# everySecond = ""

# for i in range(1, len(userInput),2) :
#     everySecond += userInput[i]
# print(everySecond)

# print(linebreak, space)

# vowels = "aeiouAEIOU"
# input_string = input("Opp C: Enter a line of text with vowels: ")
# result = ""
# for char in input_string:
#     if char in vowels:
#         result += "_"
#     else:
#         result += char
# print("Input string: ", input_string)
# print("Output string: ", result)

# print(linebreak + space)

# input_string = input("Opp D: Enter a line of text with digit: ")
# count = 0
# for char in input_string:
#     if char.isdigit():
#         count += 1
# print("The number of digits in the string is:", count)

# print(linebreak + space)

# input_string = input("Opp E: Enter a line of text with vowels: ")
# vowels = "aeiouAEIOU"
# count = 0
# for char in input_string:
#     if char in vowels:
#         count += 1
# print("The number of vowels in the string is:", count)

#Oppgave 3
print("Oppgave 3: ")
name = "Harry"

for i in range(0, len(name)) :
    print(name[i])
print(linebreak, space)


#Oppgave 4
print("Oppgave 4: ")
name = "Harry"

for i in reversed(range(0, len(name))) :
    print(name[i], end="")
print()    
print(linebreak, space)  

#Oppgave 5
print("Oppgave 5: ")

for i in range(4) :
    for x in range(i + 1) :
        print("*", end="")
    print()
print(linebreak, space)  

#Oppgave 6
print("Oppgave 6A: ")
for i in range(5):
    for j in range(5):
        if i == 0 or i == 2:
            print("X", end="")
        elif j == 2:
            break
        else:
            print("X", end="")
    print("")

print(linebreak, space)
    
print("Oppgave 6B: ")
for i in range(5):
    if i < 4:
        print("XX")
    else:
        print("XXXXX")




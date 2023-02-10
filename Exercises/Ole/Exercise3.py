#Oppgave 1
linebreak = "-----------------------"

#A
i = 0
j = 10
n = 0
print("Oppgave A")
print(linebreak)
while i < j :
  i = i + 1
  j = j - 1
  n = n + 1
  print("%3s" % str(i), "%3s" % "|" , "%3s" % str(j),"%3s" % "|","%3s" % str(n), "%3s" % "|")
  print(linebreak)

#B
i = 0
j = 0
n = 0
print("Oppgave B")
print(linebreak)
while i < 10:
    i = i + 1
    n = n + i + j
    j = j + 1
    print("%3s" % str(i), "%3s" % "|" , "%3s" % str(j),"%3s" % "|","%3s" % str(n), "%3s" % "|")
    print(linebreak)
    
#C
i = 10
j = 0
n = 0
print("Oppgave C")
print(linebreak)
while i > 0:
    i = i - 1
    n = j + 1
    j = n + i -j
    print("%3s" % str(i), "%3s" % "|" , "%3s" % str(j),"%3s" % "|","%3s" % str(n), "%3s" % "|")
    print(linebreak)
    
# #D
# i = 0
# j = 10
# n = 0
# print("Oppgave D")
# print(linebreak)
# while i != j:
#     i = i + 2
#     n = j - 2
#     j = n + 1
#     print("%3s" % str(i), "%3s" % "|" , "%3s" % str(j),"%3s" % "|","%3s" % str(n), "%3s" % "|")
#     print(linebreak)
print(linebreak)
print(" ")


# #Oppgave 2
# print("Oppgave 2")
# userInput = int(input("Enter a number: "))
# print(linebreak)
# square = 0

# while square * square < userInput:
#   square = square + 1
#   print(square * square)

# print(linebreak)
# print(" ")

#Oppgave 3
print("Oppgave 3")

c = 0
f = 0
maxGrense = int(input("Enter max: "))
print(linebreak + "---------")
print("%s" % "|","%5s" % "Celsius", "%6s" % "|", "%5s" % "Fahrenheit", "%4s" % "|")
print(linebreak + "---------")

while c <= maxGrense:
    f = c * (9/5) + 32
    print("%s" % "|", "%8s" % str(c), "%5s" % "|", "%10s" % str(f), "%4s" % "|")
    print(linebreak + "---------")
    c = c + 10


#Oppgave 4
first_name = "Harry"
last_name = "Morgan"
scores = [94, 71, 86, 95, -1]

total = 0
count = 0

while scores[count] != -1 :
    total += scores[count]
    count += 1
    i += 1

average = total/count
print(" ")
print("Oppgave 4")
print(linebreak)
print("Average score for", first_name, last_name, "is", average)


#Oppgave 5
print(" ")
print("Oppgave 5")
print(linebreak)

s = input("Enter a string: ")
uppercase_letters = ""
i = 0
while i < len(s):
    if s[i].isupper():
        uppercase_letters += s[i]
    i += 1
print("Uppercase letters:", uppercase_letters)


s = input("Enter a string: ")
every_second_letter = ""
i = 1
while i < len(s):
    every_second_letter += s[i]
    i += 2
print("Every second letter:", every_second_letter)


s = input("Enter a string: ")
vowels = "aeiouAEIOU"
new_s = s
i = 0
while i < len(vowels):
    new_s = new_s.replace(vowels[i], "_")
    i += 1
print("String with vowels replaced:", new_s)



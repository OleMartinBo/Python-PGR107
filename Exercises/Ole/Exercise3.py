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


#Oppgave 2
print("Oppgave 2")
userInput = int(input("Enter a number: "))
print(linebreak)
square = 0

while square * square < userInput:
  square = square + 1
  print(square * square)

print(linebreak)
print(" ")

#Oppgave 3
print("Oppgave 3")
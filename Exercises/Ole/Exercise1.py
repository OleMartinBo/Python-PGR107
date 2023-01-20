from math import sqrt

#Oppgave 1
#Variabler
x = 2.5
y = -1.5
m = 18
n = 4
spaceBetween = "----------"
print("Oppgave 1")
#A
opA = x + n * y - (x+n) * y
print("Answer A: " + " " + str(opA))
#B
print(spaceBetween)
opB = m // n + m % n
print("Answer B: " + " " + str(opB))
#C
print(spaceBetween)
opC = 5 * x - n / 5
print("Answer C: " + " " + str(opC))
#D
print(spaceBetween)
opD = 1 - (1 - (1 - (1 - (1 - n)))) 
print("Answer D: " + " " + str(opD))
#E
print(spaceBetween)
opE = (sqrt((n)))
print("Answer E: " + " " + str(opE))
print(spaceBetween)
print(" ")


#Oppgave 2
#Nye variabler 
n = 17
m = 18

print("Oppgave 2")
#A
print(spaceBetween)
oppA = n // 10 + n % 10
print("Answer A: " + " " + str(oppA))

#B
print(spaceBetween)
oppB = n % 2 + m % 2
print("Answer B: " + " " + str(oppB))

#C
print(spaceBetween)
oppC = (m+n) // 2
print("Answer C: " + " " + str(oppC))

#D
print(spaceBetween)
oppD = (m + n) / 2
print("Answer D: " + " " + str(oppD))

#E
print(spaceBetween)
oppE = int(0.5 *(m +n))
print("Answer E: " + " " + str(oppE))

#F
print(spaceBetween)
oppF = int(round(0.5 *(m +n)))
print("Answer F: " + " " + str(oppF))


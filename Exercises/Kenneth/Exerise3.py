
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
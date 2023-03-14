
"""
PROGRAMMING WITH NUMBERS AND STRINGS

"""

# print("----- oppgave 1 -----")

# from cmath import sqrt


# x = 2.5
# y = -1.5
# m = 18
# n = 4

# #A

# print(x + n * y - (x + n) * y )

# #B
# print(m // n + m % n)

# #C
# print(5*x-n/5)

# #D
# print(1-(1-(1-(1-(1-n)))))

# #E
# oppE = sqrt (n)
# print(oppE)

# print("-----Slutt på oppgave 1 -----")


#Oppgave 2

# from re import S


# print("----- oppgave 2 -----")


# n = 17
# m = 18 

# #A
# print(n // 10 + n % 10)

# #B
# print(n % 2 + m % 2)

# #C
# print((m+n)//2)

# #D
# print((m+n) / 2.0)

# #E
# print(int(0.5*(m+n)))

# #F
# print(int(round(0.5 *(m+n))))

# print("----- Slutt på oppgave 2 -----")

# #Oppgave 3
# print("----- oppgave 3 -----")

# s= "Hello"
# t = "World"

# #A
# print(len(s) + len(t))

# #B
# print(s[1] + s[2])

# #C
# print(s[len (s) // 2])

# #D
# print(s + t)

# #E
# print(t + s)

# #F
# print(s * 2)

# # print("----- Slutt på oppgave 3-----")


#Oppgave 4 

# n1 = int(input("Enter number 1: "))
# n2 = int(input("Enter number 2: "))

# print(f"You have entered {n1} as number 1, and {n2} as number 2. The result will then be: ")

# print("Sum of the two numbers:", n1+n2)
# print("Difference between the numbers:", n1-n2)
# print("Product:", n1*n2)
# print("The average:", (n1+n2)/2)
# print("Distance:", abs(n1-n2))

# maxNumber = max(n1, n2)
# print("Maximum number:", maxNumber)

# minNumber = min(n1, n2)
# print("Minimum number:", minNumber)


#Oppgave 5

# print("______________________")
# n1 = int(input("Enter number 1: "))
# n2 = int(input("Enter number 2: "))

# print("\n")
# print("%-15s" % "Sum:", n1+n2)
# print("%-15s" % "Difference:", n1-n2)
# print("%-15s" % "Product:", n1*n2)
# print("%-15s" % "Average:", (n1+n2)/2)
# print("%-15s" % "Distance:", abs(n1-n2))
# print("%-15s" % "Max:", max(n1, n2))
# print("%-15s" % "Min:", min(n1, n2))
# print("______________________")

#Oppgave 6

# length = int(input("Enter length of rectangle: "))
# width = int(input("Enter width of rectangle: "))

# area = length * width
# perimeter = 2*(length + width)

# print("____________Result_______________")
# print("The area of the rectangle:", area)
# print("The perimeter of the rectangle:", perimeter)
# print("_________________________________")


#Oppgave 7

# word = "kattepus"

# lengthOfWord = len(word)

# print(word[0] + word[1] + "..."+ word[lengthOfWord-2] + word[lengthOfWord-1])

#Oppgave 8

digits = input("Enter a positive number with five digits: ")
print(digits[0], digits[1],digits[2], digits[3], digits[4])
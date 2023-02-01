# oppgave1
# from cmath import sqrt


# n = 1
# m = -1

# if n < -m :
#     print(n)
# else : 
#     print(m)

# if -n >= m : 
#     print(n)
# else :
#     print(m)

# x = 0.0
# y = 1.0
# if abs(x - y) < 1 :
#     print(x)
# else :
#     print(y)

# x = sqrt(2.0)
# y = 2.0

# if x * x == y :
#     print(x)
# else :
#     print(y)

# oppgave2

# inputNumber = int(input("Enter number between 1 and 10 ---> "))

# if inputNumber < 1 : 
#     print("The number you entered is <1")
# elif inputNumber > 10 : 
#     print("The number is > 10")
# else:
#     print("The number is", inputNumber)

#oppgave 3

# number = int(input("Enter the score 0-100: "))

# if number > 100 :
#     print("invalid number")
# elif number >=90 :
#     print("The letter grade is A")
# elif number >= 80 : 
#     print("The letter grade is B")
# elif number >= 70 :
#     print("The lettr grade is C")
# elif number >= 60 : 
#     print("The letter grade is D")
# elif number < 0:
#     print("invalid number")
# else:
#     print("The letter grade is F")

#oppgave 4.

#oppgave 5.


#oppgave 6.

string = input("enter a string (it can contain both numbers/lower/uppercase letters): ")

if string.isalpha():
    print(f"The string {string} containts only letters")
else:
    print(f"The atring {string} does not have only letters.")

if string.isupper():
    print("Contain only uppercase letters")
else:
    print("The string does not only contain uppercase letters")

if string.islower():
    print("The string contains only lowercase letters.")
else:
    print("the string does not only containt lowercase letters")

if string.isdigit():
    print("The string contains only numbers")
else:
    print("the string does not only contain numbers")

if string.isalnum():
    print("The string only contains letters AND digits")
else:
    print("it does not only have letters and digits")

if string[0].isupper():
    print("The string start with a uppercase letter")
else:
    print("does not start with upperc.")

if string.endswith("."):
    print("the string ends with a period.")
else:
    print(f"The string {string} does not end with a period. :-)))")




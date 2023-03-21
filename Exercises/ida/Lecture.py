# # CODE IN LECTURES 
# # 
# # LECTURE 3: DECISIONS 

# #compare - discount
# #compute the discount for a given purchase 

# originalPrice = float(input("Original price before discount: "))

# if originalPrice < 128:
#     discountRate = 0.92
# else:
#     discountRate = 0.84

# discountPrice = discountRate * originalPrice
# print("Discounted price: %.2f" % discountPrice)


# #Even - Odd

# a = int(input("Enter a number: "))

# if a % 2 == 1:
#     print(a, "is an odd number.")
# else:
#     print(a, "is an Even number.")

# #Middle charater in string

# string = input("Enter a string:")

# position = len(string) // 2

# if len(string) % 2 == 1:
#     result = string[position]
# else:
#     result = string[position-1] + string[position]

# print("Middle charecters in '%s' is '%s'" % (string, result))


# #Tax Calculation

# RATE1 = 0.10
# RATE2 = 0.25
# RATE1_SINGLE_LIMIT = 32000
# RATE1_MARRIED_LIMIT = 64000

# income = float(input("Please enter your income: "))
# marital_status = input("Please enter s for single, m for married: ")

# tax1 = 0
# tax2 = 0

# if marital_status == "s":
#     if income <= RATE1_SINGLE_LIMIT:
#         tax1 = RATE1 * income
#     else: 
#         tax1 = RATE1 * RATE1_SINGLE_LIMIT
#         tax2 = RATE2 * (income - RATE1_SINGLE_LIMIT)

# else: 
#     if income <= RATE1_MARRIED_LIMIT:
#         tax1 = RATE1 * income
#     else:
#         tax1 = RATE1 * RATE1_MARRIED_LIMIT
#         tax2 = RATE2 * (income - RATE1_MARRIED_LIMIT)

# total_tax = tax1 + tax2
# print("the tax is $%.2f" % total_tax)


# #VALIDATION userInput

# #number
# user_input = input("Enter a number: ")

# if user_input.isdigit():
#     number = int(user_input)
#     print(number)
# else:
#     print("you did not enter a number")

# #Floating point number
# user_input = input("Enter a floating point number: ")

# if user_input.replace(".", "").isdigit():
#     number = float(user_input)
#     print(number)
# else:
#     print("Something")


# #Richter Scale 
# # This program prints a description of an earthquake, given the Richter scale 
# # magnitude.
# #
# richter = float(input("Enter a magnitude on the Richter scale: "))

# if richter >= 8.0:
#     print("Most structures fall")
# elif richter >= 7.0:
#     print("Many buildings destroyed")
# elif richter >= 6.0:
#     print("Many buildings considerably damaged, some collapse")
# elif richter >= 4.5:
#     print("Damage to poorly constructed buildings")
# else :
#     print("No destruction of buildings")


# #Substrings

# theString = input("Enter a string: ")
# theSubString = input("Enter a substring: ")

# if theSubString in theString:
#     print("The string does contain the substring")

#     howMany = theString.count(theSubString)
#     print("It containts", howMany, "instances")

#     where = theString.find(theSubString)
#     print("The first occurence starts at position", where)

#     if theString.startswith(theSubString):
#         print("the string strarts with the substring.")
#     else:
#         print("the string does not starts with the substring.")

#     if theString.endswith(theSubString):
#         print("The string ends with the substring.")
#     else:
#         print("the string does not end with the substring.")

# else:
#     print("The string does not contain the substring.")



# #Lecture 5 - functions 

# def boxString(content):
#     n = len(content)
#     if n == 0:
#         return
#     print("-" * (n+2))
#     print("!" + content + "!")
#     print("-" * (n+2))
# boxString("Hello")


# smallest = int(input("enter a value: "))
# inputStr = input("enter a value: ")

# while inputStr != "" :
#     value = int(inputStr)
#     if value < smallest :  #mhvis verdi er mindre enn 
#         smallest = value
#     inputStr = input("Enter a value: ")

    
# value = int(input("enter a value: "))
# inputStr = input("Enter a value: ")

# while inputStr != "" : 
#     previous = value
#     value = int(inputStr)
#     if value == previous :
#         print("dublicate input")
#     inputStr = input("enter a value: ")


# def boxString(contents) :
#     n = len(contents)
#     print("-" * (n + 2))
#     print("!" + contents + "!")
#     print("-" * (n+2))

# boxString(input("Enter somthing: "))
# print(boxString)


# def headingTask(contents) :
#      n = len(contents)
#      print("-" * (n))
#      print(contents)
#      print("-" * (n))

# headingTask("Task 1")
# print(headingTask)   


#Forelesning lists

#set


"""
LECTURE DICTIONARY

"""
def main():
    dictionary = {
        "0": "Zero",
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine"
    }
    
    phone_number = input("Enter ypur phone number: ")

    result = translate (dictionary, phone_number)

    print("Ypur phone number is: ", result )

def translate(dictionary, phone_number):
    result = ""
    for char in phone_number:
        result += dictionary.get(char, "???") + " "

    return result


main()
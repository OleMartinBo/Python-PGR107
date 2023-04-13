"""
SETS & DICTIONARIES 

"""

#Task 1. 

def task_1():
    set1 = {1, 2, 3, 4, 5}
    set2 = {2, 4, 6, 8}
    set3 = {1, 5, 9, 13, 17}

    # a. Is set1 a subset of set2?
    #The issubset() method returns True if all items in the set exists in the specified set, otherwise it returns False.

    print(set1.issubset(set2))

    # b. Is the intersection of set1 and set3 empty?
    #The intersection() method returns a set that contains the similarity between two or more sets. 
    # Meaning: The returned set contains only items that exist in both sets, or in all sets if the comparison is done with more than two sets.

    print(set1.intersection(set3))

    # c. What is the result of performing set union on set1 and set2?
    #The union() method returns a set that contains all items from the original set, and all items from the specified set(s). 

    print(set1.union(set2))

    # d. What is the result of performing set intersection on set2 and set3?

    print(set2.intersection(set3))

    # e. What is the result of performing the set difference on set1 and set2 (set1 – set2)?
    #The difference() method returns a set that contains the difference between two sets.
    #Meaning: The returned set contains items that exist only in the first set, and not in both sets.

    print(set1.difference(set2))

#task_1()


#Task 2. 
""" 
Given a dictionary
grade_count = {“A”: 8, “D”: 3, “B”: 15, “F”: 2, “C”: 6}
write the python statement(s) to print:

"""

def task2():
    grade_count = {"A": 8, "D": 3, "B": 15, "F": 2, "C": 6}


# a. All the keys.

    print(grade_count.keys())

# b. All the values.
    print(grade_count.values())

# c. All the key and value pairs.

    print(grade_count.items())
    
# d. All the key and value pairs in key order.
    print(sorted(grade_count.items()))

# e. The average value.

    total = 0
    for value in grade_count.values():
        total += value

    avg = total / len(grade_count)
    print("Average value = ", avg)

# f. A chart similar to the following in which each row contains a key followed by a number of asterisks
# equal to the keys data value. The rows should be printed in key order, as shown below.

# A: ********
# B: ***************
# C: ******
# D: ***
# F: **

    for key in sorted(grade_count.keys()):
        print(key + ":", "*" * grade_count[key])

#task2()

#Task 3. Write a program using dictionary that translates phone numbers in digits (entered by the user) to words.
# Sample run:
# Phone Number: 1234
# One Two Three Four

def task3():

    number = input("Phone Number: ")

    digits_chr = {
        "1" : "en",
        "2": "to",
        "3": "tre",
        "4": "fire",
        "5": "fem",
        "6": "seks",
        "7": "syv",
        "8": "åtte",
        "9": "ni"
    }

    result = ""

    for ch in number:
        result += digits_chr.get(ch, "?") + " "  #? kommer hvis input ikke er et tall
    print(result)

#task3()

#Task 4. 4. Write a program that keeps a dictionary in which both keys and values are strings—names of students and
# their course grades. Prompt the user of the program to add or remove students, to modify grades, or to
# print all grades. The printout should be sorted by name formatted like this:
# Carl: B+
# Francine: A
# Joe: C
# Sarah: A



    
def task4():
    students_dictionary = {
        "Carl": "B+",
        "Sarah": "A",
        "Ida": "A",
        "Ole": "B",
        "Eva": "C"
    }

    while True:
        userInput = input("Your choices: \n -add students(1) \n -remove students(2), \n -modify grades(3), \n -print all grades(4) \n -quit(Q) \n")
    
        if userInput == "1":
            new_student = input("Enter a new student: ")
            new_value = input("Enter students grade: ")
            students_dictionary[new_student] = new_value
            
            for key in sorted(students_dictionary):
                print(f"{key}: {students_dictionary[key]}")
        elif userInput == "2":
            remove = input("Enter a students name to remove them from list: ")
            if remove in students_dictionary:
                students_dictionary.pop(remove)
            else:
                print("The student is not in list.")
            for key in sorted(students_dictionary):
                print(f"{key}: {students_dictionary[key]}")
        elif userInput == "3":
            modify = input("Enter name to modify grades: ")
            if modify in students_dictionary:
                grade = input("Enter new grade: ")
                students_dictionary[modify] = grade
            for key in sorted(students_dictionary):
                print(f"{key}: {students_dictionary[key]}")
        elif userInput == "4":
            for key in sorted(students_dictionary):
                print(f"{key}: {students_dictionary[key]}")
        elif userInput.upper() == "Q":
            break
        else:
            print("invalid input")

#task4()

#Task 5. 
# Consider a dictionary of different usernames (keys) and passwords (values). Write a function called accept_login ()
#  with three parameters: the dictionary, a username, and a password. The function should return True if
#  the user exists and the password is correct, then the message “Login Successful” is printed. Otherwise, the function returns False, 
# then the message “Login Failed” is printed.

def task5():

    users_dictionary = {
        "Ida" : "123",
        "Skip": "456",
    }

    username = input("Enter username: ")
    password = input("Enter password: ")

    if accept_login(users_dictionary, username, password):
        print("Login successful")
    else:
        print("Login Failed")


def accept_login(users_dictionary, username, password):
 
    if username not in users_dictionary:
        return False
    else:
        if users_dictionary[username] == password:
            return True
        else:
            return False

#task5()

#Task 6.
# Write a function def one_to_one (d) that takes a dictionary d and returns True if every value in d has only one corresponding key. 
# For example, if d = {'a': 4, 'b': 5, 'c': 3}, 
# the function returns Ture but if d = {'a': 2, 'b': 4, 'c': 2}, the function returns False.


def task6():
    # dictionary = {
    #     "a": 4,
    #     "b": 5,
    #     "c": 3
    # }

    dictionary = {
        "a": 2, 
        "b": 4, 
        "c": 2
        }

    print(one_to_one(dictionary))

def one_to_one(d):
    seen = set()
    for value in d.values():
        if value in seen:
            return False
        seen.add(value)
    return True

task6()



"""
lIST, TUPLEST AND SETS 

"""

import collections
from os import remove
from random import randint
import random


a = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]

"""
print("a")
print("-" * 10)

total = 0
for i in range(10):
    total = total + a[i]
    print(total)

print("b")
print("-" * 10)

total = 0 
for i in range(0, 10, 2): #med tre argument viser 2 til antall steg: 0, 2, 4, 6 oh 8
    total = total + a[i]
    print(total)

print("c")
print("-" * 10)

total = 0 
for i in range(1, 10, 2) : 
    total = total + a[i]
    print(total)

print("d")
print("-" * 10)

total = 0 
for i in range(2, 11): 
    total = total + a[i]
    print(total)

print("e")
print("-" * 10)

total = 0 
i = 1
while i < 10 : 
    total = total + a[i] 
    i = 2 * i
    print(total)

print("f")
print("-" * 10)


total = 0
for i in range(9,-1, -1) : 
    total = total + a[i]
    

print("g")
print("-" * 10)

total = 0
for i in range(9, -1, -2) : 
    total = total + a[i]
    print(total)

print("h")
print("-" * 10)

total = 0 
for i in range(0, 10) : 
    total = a[i] - total
    print(total)

  
"""

"""
#Task 2


# Write a program using a loop that fills an empty list called values with ten random numbers between 1 and 100.

values = []

for i in range(10):
    values.append(randint(1,100))
print(values, end=" ")



# task 3 - for loops
# Write programs using for loops (WITHOUT range function) that iterate over the list
# generated in Exercise 2 (values) and do the following tasks.


values = []

for i in values:        #uten range 
    if len(values) == 10:
        break
    values.append(random.randint(1, 100))
print(values, end=" ")


    
#a. printe alle elementer av listen på enkel rad

for elem in values:
    print(elem, end=" ")

#b. sum av alle elementer i listen

total = 0

for elem in values:
    total += elem
print("The sum of all elements: ", total)

#c. compute how many elements are even numbers

count = 0

for elem in values:
    if elem %2 == 0:
        count += 1
print(f" There are {count} even numbers in the list.")


#Task 4. Consider the list generated in Exercise 2 (values) and separate the even and odd numbers 
# into two different lists even_values, odd_values.

even_values = []
odd_values = []

for elem in values:
    if elem % 2 == 0:
        even_values.append(elem)
    else:
        odd_values.append(elem)

print(f"The list contains {values} values. In this list the even values are: {even_values}, and the odd values are: {odd_values}")


#Task 5. Consider the list generated in Exercise 2 (values) and remove the odd elements from the list.

print("The orginal list is: ", values)

newList = []
for elem in values:
    if not (elem % 2 != 0):
        newList.append(elem)
print("The list after removal of odd elements: ", newList)



#Task 6: Write a program that generates a sequence of 20 random values between 0 and 99,
#  stores them in a list, prints the sequence, sorts it, and prints the sorted sequence. Use the sort method.

values = []

for i in range(20):
    values.append(random.randint(0,99))
    values.sort()
print("The sorted list: ", values, end=" ")


#task 7. Write a function def same_list (a, b) that checks whether two lists have the same elements in some order,
# ignoring duplicates. For example, the two lists


def same_list(a, b):
    sorted_a = sorted(set(a))
    sorted_b = sorted(set(b))
    return sorted_a == sorted_b


a = [1, 4, 9, 16, 9, 7, 4, 9, 11]
b = [11, 11, 7, 9, 16, 4, 1]

if same_list(a, b):
    print("The lists are equal")
else:
    print("The lists are not equal")

    


#9. Write a function remove_min that removes the minimum value 
# from a list without using the min function or remove method.

def remove_min():
    value_list = [30, 50, 90, 10, 10, 20]
    print("Original list: ", value_list)

#finne min value:
    min_val = value_list[0]
    for num in value_list:
        if num < min_val:
            min_val = num

#2.sjekke gjennom hver [i] == min value + del for å fjerne den verdien som er lik
# ved å bruke break vil den exite loopen med en gang den finner matchende min value --> fjerner ikke duplikater     
    for i in range(len(value_list)):
        if value_list[i] == min_val:
            del value_list[i]
            break 
    print("List after removing min value: ", value_list )

#remove_min()

# Task 10. Write a program that removes duplicate tuples from a list of tuples.

def removeDuplicates(tupleList): 
    return list(set([i for i in tupleList])) #gjør list om til set(=unik)

tupleList = [(1, 2), (5, 7), (1, 2), (4, 3), (1, 2)]

print("The original tuple list: ", tupleList)
print("Tuple list without duplicate: ", removeDuplicates(tupleList))


""" 

#8. Write a function sum_without_smallest that computes the sum of a list of 10 random values between 1
#and 100, except for the smallest one, in a single loop. In the loop, update the sum and the smallest value.
#After the loop, subtract the smallest value from the sum and return the difference

""" 

def sum_without_smallest():
    random_lst = []
    min_val = float('inf') # returns a floating infinity value and initialize min_val with the maximum possible value --> bra å bruke for å holde på min og max verdier,fordi alt vil bli lavere

    for i in range(10):
        num = randint(1, 100)
        random_lst.append(num)
        min_val = min(min_val, num)

    Sum = sum(random_lst)
    print("Original list sum:", Sum)

    print("The minimum value in list: ", min_val)

    newList = Sum - min_val

    print("New list without smallest value: ", newList)

sum_without_smallest()

"""
import random

def sum_without_smallest():
    # initialize the sum and smallest value
    lst = [random.randint(1, 100) for i in range(10)]
    smallest = min(lst)
    total_sum = sum(lst)
    
    # compute the sum without the smallest value
    for val in lst:
        if val == smallest:
            continue
        total_sum -= smallest
    
    return total_sum

sum_without_smallest()
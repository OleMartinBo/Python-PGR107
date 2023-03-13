a = [1,2,3,4,5,4,3,2,1,0]

def A():
    total = 0
    for i in range(10):
        total = total + a[i]
    return total

# print(A())

def B():
    total = 0
    for i in range(0,10,2):
        total = total + a[i]
    return total

# print(B())

def C():
    total = 0
    for i in range(1,10,2):
        total = total + a[i]
    return total

# print(C())

def D():
    total = 0
    for i in range(2,11):
        total = total + a[i]
    return total

# print(D())

def E():
    total = 0
    i = 1
    while i < 10 :
        total = total + a[i]
        i = 2 * i
    return total

# print(E())

def F():
    total = 0
    for i in range(9, -1, -1):
        total = total + a[i]
    return total

# print(F())

def G():
    total = 0
    for i in range(9, -1, -2):
        total = total + a[i]
    return total

# print(G())

def H():
    total = 0
    for i in range(0, 10):
        total = a[i] - total
    return total

#print(H())

#Oppgave 2 Write a program using a loop that fills an empty list called  values with ten random numbers between 1 and 100. 
import random 
randomLists = []
def loopyloop():
    
    for i in range(10):
        randomLists.append(random.randrange(1,100))
    

loopyloop()


def iterateLoopyLoop1():
    
    for element in randomLists:
            print(element, end=" ")

# print(iterateLoopyLoop1())

def iterateLoopyLoop2():
    total = 0
    for element in randomLists:
        total = total + element
    
    return total

# print(iterateLoopyLoop2())

def iterateLoopyLoop3():
    count = 0
    for element in randomLists:
        if element % 2 == 0:
            count = count + 1
    
    return count

# print(iterateLoopyLoop3())
            
#Oppgave 3 Consider the list generated in Exercise 2 (values) and separate the even and odd numbers into two different lists even_values, odd_values

def evenOrOdd():
    evenValues = []
    oddValues = []
    for element in randomLists:
        if element % 2 == 0:
            evenValues.append(element)
        else:
            oddValues.append(element)

    print(f"This is evenValues: {evenValues}\nThis is oddvalues:  {oddValues}")
    
# evenOrOdd()

def removeOdd():
    
    for element in randomLists:
        if element % 2 == 1:
            
            randomLists.remove(element)      
    
    print(f"{randomLists}")

# removeOdd()
sortingList = []
def sorting(): 
    for i in range(20):
        sortingList.append(random.randrange(0,99))
    print(f"This is the unsorted list: {sortingList}")
    sortingList.sort()
    print(f"This is the sorted list:   {sortingList}")

sorting()





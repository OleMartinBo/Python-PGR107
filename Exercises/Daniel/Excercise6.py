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
    i = 0
    print(f"This is the old list: {randomLists}")
    while i < len(randomLists):
        if randomLists[i] % 2 == 1:
            randomLists.pop(i)
        else: 
            i += 1     
    
    print(f"This is the new list: {randomLists}")

# removeOdd()
sortingList = []
def sorting(): 
    for i in range(20):
        sortingList.append(random.randrange(0,99))
    print(f"This is the unsorted list: {sortingList}")
    sortingList.sort()
    print(f"This is the sorted list:   {sortingList}")

# sorting()

firstList = [1,4,9,16,9,7,4,9,11]
SecondList = [11,11,7,9,16,4,1]

def isSameList(a,b):
    
    if a == b:
        print("It's the same list")
    else:
        print("It's not the same list")
    
    
# isSameList(firstList, SecondList)


# Oppgave 8

def sumWithoutMin():
    randomList = []
    sum = 0
    
    for i in range(10):
        randomList.append(random.randint(1,100))
    
    randomList.sort()
    minNum = min(randomList)
    print(randomList)
    for element in randomList:
        if element == randomList[0]:
            randomList.pop(0)
        else:
            sum = sum + element
    
    sum = sum - randomList[0]
    print(f"The Sum is: {sum}")

# sumWithoutMin()
list1 = [(1,2), (4,3), (5,6), (1,2), (3,4)]
def isDoubleTuple():
    list2 = []
    for tuple in list1:
        if tuple in list2:
            list1.remove(tuple)
        else:
            list2.append(tuple)
    return list2

# print(isDoubleTuple())

def generateRaise(rate):
    
    rate = float(input("Is your interest 0.0 0.4 or 0.6? "))
    
    if rate == 0.0:
        pass
        
        
    
    




#Oppgave 1
def oppone() :
    a = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
    total = 0
    
    #Sum av alle tallene i list
    for i in range(10) :
        total = total + a[i]
    print(total)

    #
    for i in range(0,10,12) :
        total = total + a[i]
    print(total)

    #Øker med to fra index/element/objekt plassert på 1 opp til 10
    for i in range(1,10,2) :
        total = total + a[i]
    print(total)
    
    #Error pga range er ute av rangen fra 0 - 10. Ingen index/element/objekt plassert på 11
    #for i in range(2,11) :
        #total = total + a[i]
    #print(total)
        
    #
    i = 1
    while i < 10 :
        total = total + a[i]
        i = 2 * i
    print(total)
    
    #
    for i in range(9, -1, -1) :
        total = total + a[i]
    print(total)
    
    #
    for i in range(9, -1, -2) :
        total = total + a[i]
    print(total)
    
    #
    for i in range(0, 10) :
        total = a[i] - total
    print(total)
    
#oppone()

#oppgave 2, 3, 4 og 5
def listTypes():
    from random import randint
    values = []
    i = 0
   
    while i < 10 :
        value = randint(1, 100)
        values.append(value) 
        i += 1        
    print(values)
    print(" ")

    for value in values :
        print(value, end=" ")
    print()
    print(" ")

    total = 0
    for value in values :
        total = total + value
    print(total)
    print(" ")
    
    evenNumbers = 0
    for value in values :
        if value % 2 == 0 :
            evenNumbers += 1
    print(evenNumbers)
    print(" ")
            
    evenList = []
    oddList = []
    for value in values:
        if value % 2 == 0 :
            evenList.append(value)
        else :
            oddList.append(value)
    print("Even numbers=", evenList)
    print("Odd numbers=", oddList)
    print(" ")

    for value in values:
        if value % 2 != 0 :
            values.remove(value)
    
    print("Removed odd numbers, even numbers left in list=",values)
    print(" ")
    

#listTypes()

#Oppgave 6
def sequence() :
    from random import randint
    values = []
    
    for i in range(0,20) :
        value = randint(0,99)
        values.append(value)
        values.sort()
    print("The values from lowest to highest:",values)

#sequence()
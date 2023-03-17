#Oppgave 1
def oppgave1() :
    set1 = {1, 2, 3, 4, 5} 
    set2 = {2, 4, 6, 8} 
    set3 = {1, 5, 9, 13, 17} 

    #A, sjekker om set 1 er subset av set 2
    print("Is set1 a subset of set2:",set1.issubset(set2))
    #B, Lager nytt set med duplicates
    print("intersection on set1 and set3:",set1.intersection(set3))
    #C, Fjerner duplicates
    print("union on set1 and set2:",set1.union(set2))
    #D,Lager nytt set med duplicates
    print("intersection on set2 and set3:",set1.intersection(set2))
    #E,
    print("difference on set1 and set2:",set1.difference(set2))
    
    
#oppgave1()

#Oppgave 2
def oppgave2() :
    grade_count = {'A': 8, 'D': 3, 'B': 15, 'F': 2, 'C': 6}
  
    #A
    keyList = list(grade_count.keys())
    print(keyList)
    #B
    valueList = list(grade_count.values())
    print(valueList)
    #C
    itemList = list(grade_count.items())
    print(itemList)
    #D
    for key in sorted(grade_count) :
        print(key, grade_count[key])
    #E
    average = sum(grade_count.values()) / len(grade_count)
    print("Average:", average)
    #F
    for key in sorted(grade_count):
        print(key + ":" + "*" * grade_count[key])

#oppgave2()

#Oppgvae 3
def oppgave3() :
    phone_dict = {'0': 'Zero','1': 'One','2': 'Two','3': 'Three','4': 'Four','5': 'Five','6': 'Six','7': 'Seven','8': 'Eight','9': 'Nine'}
    phone_number = input('Phone Number: ')

    words = []
    for digit in phone_number:
        words.append(phone_dict[digit])

    print(' '.join(words))

#oppgave3()

#Oppgave 4
def oppgave4() :
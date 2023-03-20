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
    students = {'Carl':'B','Francine':'A','Joe':'C','Sarah':'A'}
    
    addStudent = input("Add student: ")
    newGrade = input("Change grade to: ")
    
    students[addStudent] = newGrade
    for i in sorted(students) :
        print(i, students[i])
        
    removeStudent = input("Remove student: ")
    
    if removeStudent in students :
        students.pop(removeStudent)
    else: 
        print(removeStudent, "is not in dictionary")
        
    for i in sorted(students) :
        print(i, students[i])
    
#oppgave4()

#Oppgave 5
def oppgave5() :
    
    users = {'Ole':'12345'}
    enterName = input("Enter the username: ")
    enterPassword = input("Enter password: ")
    
    if accept_login(users, enterName, enterPassword) :
        print("Login Successful")
    else:
        print("Login Failed")   


def accept_login(users, enterName, enterPassword) :
    
    if enterName not in users :
        return False
    else :
        if users[enterName] == enterPassword :
            return True
        else :
            return False        

#oppgave5()

#Oppgvae 6
def oppgave6():
    #dictionary = {'a': 4, 'b': 5, 'c': 3}
    dictionary = {'a': 2, 'b': 4, 'c': 2}

    print(one_to_one(dictionary))
    
    
def one_to_one(d) : 
    
    seen = set() 
    for value in d.values() :
        if value in seen :
            return False
        seen.add(value)
    return True

oppgave6()

def oppgave1() :
    
    filename = "Exercises\Ole\hello.txt"
    file = open(filename, "w")
    file.write("Hello, World!")
    file.close()
    
    file = open("Exercises\Ole\hello.txt", "r")
    data = file.read()
    print(data)
    file.close()

#oppgave1()


def oppgave2() :
    
    user_file_input = input("Enter the file path: ")
    user_file_save_output = input("Enter the file path to save to: ")
    
    read = open("Exercises\Ole\input.txt", "r")
    write = open("Exercises\Ole\output.txt", "w")
    
    lineNumber = 1
    for l in read :
        write.write("/* %s */ %s" % (lineNumber, l))
        lineNumber += 1
    
    read.close() 
    write.close()

#oppgave2()

def oppgave3():
    filename = input("Enter file path: ")
    file = open(filename, "r")
    
    sumColumn1 = 0
    sumColumn2 = 0
    
    for l in file:
        l = l.split()
        sumColumn1 += float(l[0])
        sumColumn2 += float(l[1])
    
    file.close()
    
    print("Sum of column 1:", sumColumn1)
    print("Sum of column 2:", sumColumn2)
    
#oppgave3()

def oppgave4():
    
    filename = input("Enter the file path: ")
    file = open(filename, "r")
    
    numb_of_chars = 0
    numb_of_words = 0
    numb_of_lines = 0
    
    for l in file :
        numb_of_chars += len(l.strip())  
        numb_of_words += len(l.split(" "))
        numb_of_lines += 1
        
    file.close()
    print("Number of chars:", numb_of_chars, "\nNumber of words:", numb_of_words,"\nNumber of lines:", numb_of_lines)
    
#oppgave4()

def oppgave5():
    
    right_number_list = []
    chances = 2
    
    while chances != 0:
        try :
            inputFloat = float(input("Enter a number: "))
            right_number_list.append(inputFloat)
        except ValueError:
            chances -= 1
            if chances != 0:
                print("Please enter a number and try again or a char to quit: ")
    print("Sum of number list:", sum(right_number_list))

oppgave5()
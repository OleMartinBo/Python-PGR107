def filenName():
    filename = "Exercises\ida\hello.txt"
    file = open(filename, "w")
    file.write("Hello, World!")
    file.close()

    file = open(filename, "r")
    content = file.read()
    print(content)
    file.close()

#filenName()


def task2():

    fileInput = "Exercises\\ida\\inputFile.txt"
    fileOutput = "Exercises\\ida\\outPutFile.txt"

    readFile = open(fileInput, "r")
    writeToFile = open(fileOutput, "w")
    
    lines = 1
    for line in readFile:
        writeToFile.write("line %s: %s " % (lines, line))
        lines += 1

    readFile.close()
    writeToFile.close()

#task2()

def task3():
    filename = "Exercises\\ida\\floatingNumbers.txt"

    file = open(filename, "r")
    column1 = 0
    column2 = 0

    with open(filename, "r") as file:
        for line in file:
            line = line.split()
            column1 += float(line[0])
            column2 += float(line[1])
    
    column1_average = column1 / 2
    column2_average = column2 / 2

    file.close()
    print("Average of column: ", column1_average)
    print("Average of column: ", column2_average)

#task3()

def task4():
    filename = "Exercises\\ida\\hello.txt"
    
    with open(filename, "r") as file:
        char = 0
        words = 0
        lines = 0

        for line in file:
            char += len(line)
            words += len(line.split())
            lines += 1
    print("Number of char: ", char)
    print("Number of words: ", words)
    print("Number of lines: ", lines)

#task4()

def task5():
    total = 0
    tries = 0

    while tries < 2:
        value = input("Enter a floating point value: ")
        if not value:
            break
        try:
            total += float(value)
            tries = 0
        except ValueError:
            tries += 1
            print("Invalid input. Enter floating point value.")
    print("Sum is: ", total)

#task5()

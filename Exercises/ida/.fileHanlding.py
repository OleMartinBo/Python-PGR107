
""" FILE OBJECTS - READING AND WRITING TO FILE"""

#filename = "Exercises\\ida\\hello.txt"

def readAll(): 
# Åpner alt som står i fil: 
    with open(filename, "r") as f:
        f_contents = f.read()
        print(f_contents)

#readall()

def readlines(): 
#Leser alle linjene i filen
    with open(filename, "r") as f:
        for line in f: 
            print(line, end="")

#readlines()


def specifyAmountOfLines():
    with open(filename, "r") as f:
        f_contents = f.read(3)  #leser 3 første bokstaver i filen
        print(f_contents, end="")
#specifyAmountOfLines()

def test():
    #Funker ikke - skriver bare alt til fil
    with open(filename, "r") as f:
        SIZE_TO_READ = 1
        f_contents = f.read(SIZE_TO_READ)

        while len(f_contents) > 0:
            print(f_contents, end="")
            f_contents = f.read(SIZE_TO_READ)
#test()

"""WRITE TO FILE"""

filename = "Exercises\\ida\\test2.txt"

def writeToFile():
    with open(filename, "w") as f:
        f.write("test")

#writeToFile()

def both():
    readFile = "Exercises\\ida\\hello.txt"
    writeToFile = "Exercises\\ida\\test2.txt"
    
    with open(readFile, "r") as rf:  #original file
        with open(writeToFile, "w") as wf: #Copy file that dosent exist. 
            for line in rf:
                wf.write(line) #Skriver det som står i orginal fil over til copy fil.

#both()
"""
"""


def chunckSize():
    #Funker ikke - skriver bare alt til fil
    readFile = "Exercises\\ida\\hello.txt"
    writeToFile = "Exercises\\ida\\test2.txt"
    
    with open(readFile, "r") as rf:  
        with open(writeToFile, "w") as wf: 
            chunk_size = 2
            rf_chunk = rf.read(chunk_size)

            while len(rf_chunk) > 0:
                wf.write(rf_chunk)
                rf_chunk = rf.read(chunk_size)
chunckSize()


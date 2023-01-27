import os

path = os.path.join(os.getcwd(), "selvstudie\Daniel")
fileName = "nyFilTest.txt"
filePath = os.path.join(path, fileName)
    
with open(filePath, "w") as file:
    file.write("Hello")
    
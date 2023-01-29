import os

from isort import file

class makeFiles: 
    def __init__(self, name, content, path):
        self.name = name
        self.content = content
        self.path = path
        
  
        
    def createFile(self):
        with open(os.path.join(self.path,self.name), "w") as f:
            f.write(self.content)
    
    def add_to_file(self):
        with open(os.path.join(self.path,self.name), "a") as f:
            f.write("\n" + self.content)
            
testFile = makeFiles("pleaseWork.txt", "This is a test", 'selvstudie\Daniel')
#write = makeFiles("DanielpleaseWork")

addContent = makeFiles("pleasework.txt", "Here i add content", 'selvstudie\Daniel')

#testFile.createFile()

addContent.add_to_file()
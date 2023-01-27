
class animal:
    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year
        
        
        
    def speak(self, times: int = 1):
        pass
    
    
class Dog(animal):
    def speak(self, times: int = 1):
        return "WOOF" *times

class Cat(animal):
    def speak(self, times: int = 1):
        return "MEOW" *times  
    
dog = Dog("Oblix", "Black", 2015)
print("%-20s" % "The dogs name is:", dog.name)
print("%-20s" % "The dogs color is:", dog.color)
print("%-20s" % "The dogs born in", dog.year )
print("%-20s" % "The dog says", dog.speak(7))

cat = Cat("Pusur", "Brown", 2017)
print(cat.speak(50))
    
        
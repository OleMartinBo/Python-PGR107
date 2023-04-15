class Robot:
    def __init__(self, name, color, weight):
        self.name = name                        #self = this i java
        self.color = color
        self.weigt = weight
    
    def __str__(self):
      return f"my name is {self.name}, and my favorite color is {self.color}, and i weight {self.weigt} kg"

    

r1 = Robot("Tom", "Red", 50)
r2 = Robot("Ida", "Rosa", 40)

print(r1)
print(r2)

class Robot:
    def __init__(self, name, color, weight):
        self.name = name                        #self = this i java
        self.color = color
        self.weigt = weight
    
    def introduce_self(self):
        print(f"My name is {self.name}, and my facorite color is {self.color}. I weight {self.weigt} kg")

    

r1 = Robot("Tom", "Red", 50)
r2 = Robot("Ida", "Rosa", 40)

r1.introduce_self()
r2.introduce_self()


### Tally counter

#Oppgave 1 

"""
class Counter:
    def reset(self):
        self.value = 0
        self.prev_value = 0
    
    def click(self):
        self.prev_value = self.value
        self.value += 1
    
    def undo(self):
        if self.value > self.prev_value:
            self.value = self.prev_value
    
    def get_value(self):
        return self.value
    
tally = Counter()
tally.reset()

tally.click() # 1
tally.click() # 2
print(tally.get_value()) # 2

tally.undo() # undo 1 click
print(tally.get_value()) # 1

tally.click() # 2
tally.click() # 3
print(tally.get_value()) # 3

tally.undo() # undo 1 click
print(tally.get_value()) # 2

tally.reset() # 0
print(tally.get_value()) # 0

#Oppgave 2

class Adress:
    def __init__(self, house_num, street, city, state, postal_code):
        self.house_num = house_num
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.apt_num = None
    
    def set_apt_num(self, apt_num=""):
        self.apt_num = apt_num

    def print_adress(self):
        adressline_1 = f"{self.house_num} {self.street}"
        if self.apt_num is not None:
            adressline_1 += f" Apartment number: {self.apt_num}"
        adressline_2 = f"{self.city}, {self.state}, {self.postal_code}"
        print("adressline 1: ", adressline_1)
        print("Adressline 2: ", adressline_2)

    def comesBefore(self, other):
        return self.postal_code < other.postal_code


a1 = Adress(20, "Langhusveien", "Langhus", "Norway", "1405")
a2 = Adress(30, "Wesselsvei", "Vestby", "Norway", "1540")
a2.set_apt_num("B")
a1.set_apt_num("10C")

a1.print_adress()
a2.print_adress()

print(a1.comesBefore(a2))

"""

#Oppgave 3

class Car:
    def __init__(self, fuel_efficiency):
        self.fuel_efficiency = fuel_efficiency
        self.fuel_level = 0
    
    def drive(self, distance):
        fuel_needed = distance / self.fuel_efficiency
        if fuel_needed > self.fuel_level:
            print("Not enough fluel!")
        else:
            self.fuel_level -= fuel_needed

    def getGasLevel(self):
        return self.fuel_level
    
    def addGas(self, gallons):
        self.fuel_level += gallons
    
  
myHybrid = Car(50)
myHybrid.addGas(20)
myHybrid.drive(100)
print(myHybrid.getGasLevel())

#Oppgave 4

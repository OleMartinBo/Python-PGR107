#Oppgave1
class Counter:
    def __init__(self):
        self.value = 0
        
    def reset(self):
        self.value = 0
    
    def click(self):
        self.value = self.value + 1
        
    def undo(self):
        if self.value > 0:
            self.value = self.value -1
        else:
            print("Cant sub lower than zero")
    
    def get_value(self):
        return self.value
    
def oppgave1():   
    tally = Counter()
    tally.undo()
    tally.reset()
    tally.click() # 1
    tally.click() # 2

    print(tally.get_value()) # 2
    tally.click() # 3
    print(tally.get_value()) # 3
    tally.click() 
    print(tally.get_value()) # 4
    tally.undo() #-1
    print(tally.get_value()) # 3
    tally.reset() # 0

    print(tally.get_value()) # 0

#oppgave1()

#Oppgave 2
class Address:
    def __init__(self, house_number, street, city, state, postal_code):
        self.house_number = house_number
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.apartment_number = None
        
    def set_aptNumb(self, apartment_number=""):
        self.apartment_number = apartment_number
        
    def print_address(self):
        if self.apartment_number is not None:
            print(f"{self.house_number} {self.street}, Apt {self.apartment_number}")
        else:
            print(f"{self.house_number} {self.street}")
        print(f"{self.city}, {self.state} {self.postal_code}")

    def comes_before(self, other):
        return self.postal_code < other.postal_code
    

p1 = Address(12,"gjerdumsvei","oslo","nogre", 0)

p1.set_aptNumb("G")

p1.print_address()


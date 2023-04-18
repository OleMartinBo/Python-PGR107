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
    def __init__(self, house_number, street, city, state, postal_code, apartment_number = 0):
        self.house_number = house_number
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.apartment_number = apartment_number
        
    def get_postal_code(self):
        return self.postal_code
        
    def print_address(self):
        if self.apartment_number == 0:
            return f"House number: {self.house_number}, Street: {self.street}\nCity: {self.city}, State: {self.state}, Postal code: {self.postal_code}"
        
        return f"Street: {self.street}, House Number: {self.house_number}, Apratment Number: {self.apartment_number}\nCity: {self.city}, State: {self.state}, Postal Code: {self.postal_code}"

    def comes_before(self, other):
        if self.get_postal_code() < other.get_postal_code():
            return True
        return False        
    
def oppgave2():
    p1 = Address("Oslo", "Oslo", "0645", "Dronningsgata", 18)
    print(p1.print_address())
    p2 = Address("Stavanger", "Rogaland", "3657", "Holbergsgate", 33, 8976)
    print(p2.print_address())
    print(p1.comes_before(p2))

#oppgave2()


class Car:
    def __init__(self, fuel_efficieny, fuel = 0):
        self.fuel = fuel
        self.fuel_efficieny = fuel_efficieny
        
    def getGas(self):
        return self.fuel
    
    def addGas(self, amount):
        self.fuel = self.fuel + amount
        
    def moveCar(self, distance):
        if self.fuel * self.fuel_efficieny < distance:
            print("Cant drive with no fuel")
            return False
        
        self.fuel = self.fuel - distance/self.fuel_efficieny
        return True
    
def oppgave3():
    
    myHybrid = Car (50)
    myHybrid.addGas (20) 
    myHybrid.moveCar (100) 
    print(myHybrid.getGas()) 

#oppgave3()


class Letter:
    def __init__(self, letterFrom, letterTo):
        self.letterFrom = letterFrom
        self.letterTo = letterTo
        self.text = ""
        
    def addLine(self, line):
        self.text = self.text + line + "\n"
    
    def getText(self):
        textOutput = "Dear: " + self.letterTo + "\n\n"
        textOutput = textOutput + self.text 
        textOutput = textOutput  + "\n"+ "Sincerly\n\n" + self.letterFrom
        return textOutput
    

def oppgave4():
    my_letter = Letter("Marry", "John")
    my_letter.addLine("I am sorry we must part.")
    my_letter.addLine("I wish you all the best.")
    print(my_letter.getText())

#oppgave4()

class Customer:
    def __init__(self):
        self.totalPurchases = 0
    
    def getTotal(self):
        return self.totalPurchases
    
    def makePurchase(self,amount):
        if self.discountReached() :
            self.totalPurchases = self.totalPurchases + amount - 10
        else :
            self.totalPurchases = self.totalPurchases + amount
    
    def discountReached(self):
        if self.totalPurchases >= 100 :
            return True
        return False
    
def oppgave5():

    cust1 = Customer()
    
    cust1.makePurchase(102)
    print(cust1.getTotal())
    
    cust1.makePurchase(4)
    print(cust1.getTotal())
    
    cust1.makePurchase(3)
    print(cust1.getTotal())
    
#oppgave5()

    
    
class Bank:
    def __init__(self, balance = 0):
        self.balance = balance
        
    def getBalance(self) :
        return self.balance
    
    def deposit(self, amount) :
        self.balance = self.balance + amount
        
    def withdraw(self,amount) :
        PENALTY = 10
        if amount > self.balance :
            self.balance = self.balance - PENALTY
        else:
            self.balance = self.balance -amount
            
    def addInterest(self, rate) :
        amount = self.balance * rate / 100
        self.balance = self.balance + amount
        
        
        
def oppgave6():
    
    accountCheck = Bank()
    
    accountCheck.deposit(2500)
    print(accountCheck.getBalance())
    accountCheck.withdraw(500)
    print(accountCheck.getBalance())
    accountCheck.addInterest(2)
    print(accountCheck.getBalance())
    
oppgave6()
        
        
    
    
    
    
    
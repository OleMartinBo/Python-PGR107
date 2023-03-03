from random import randint

#Variabler 
value = randint(1,1000)
counter = 0





while counter != 5 :
    
    userIput = int(input("Enter a number: "))
    
    if userIput == value :
        print("Congratulation! You guessed the number in:", counter ,"attempt(s)”",)
    elif userIput < value :
        print("The number is Higher")
    elif userIput > value :
        print("The number is lower")
        
    counter += 1
    print("You got:", counter, "Wrong")

print("The number was:", value)
        
            
    


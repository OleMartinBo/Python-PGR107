# def habits(days):
#     total = 1
#     for i in range(0, days):
#         total = total * 1.01
#     return total

# userInput = int(input("How many days?: "))

# result = habits(userInput)

# print("%.2f" % result )

# Write a function that takes in a list of numbers and returns the sum of all the even numbers in the list.

def evenNumber():
    total = 0
    for num in numList:
        if num % 2 == 0:
            total += num
    return total

numbers = int(input("Write a positive number to add, or a negative number to quit: "))
numList = []
while True:
    if numbers < 0:
        break
    else:
        numList.append(numbers)
        
    numbers = int(input("Write a positive number to add, or a negative number to quit: "))
    
result = evenNumber()

print(f"The even numbers add up to: {result}")
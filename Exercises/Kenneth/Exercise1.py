from math import sqrt


# 1 What are the values of the following expressions? In each line, assume that 

x = 2.5
m = 18
n = 4
y = -1.5
spaceBetween = "----------"

#A
#print(eval("x + n * y - (x + n) * y"))
#B
#print(eval("m//n+m%n"))
#C
#print(eval("5 * x - n / 5 "))
#D
#print(1 - (1 - (1 - (1 - (1 - n)))))
#E
#print(sqrt((n)))

#2. What are the values of the following expressions, 
# assuming that n is 17 and m is 18? 

n = 17
m = 18 

#A
#print(n // 10 + n % 10 )
#B
#print(n % 2 + m % 10)
#C
#print((m + n) // 2 )
#D
#print((m + n) / 2.0 )
#E
#print( int  (0.5 * (m + n)) )
#F
#print(int (round (0.5 * (m + n))) )

#3. What are the values of the following expressions? 
# In each line, assume that 

s = "Hello"
t = "World"

#A
#result = len(s) + len(t)
#print(result)

#B 
#result = s[1]+ s[2]
#print(result)

#C
#result = s[len (s) // 2]
#print(result)

#D

#result = s + t
#print(result)

#E 
#result = t + s 
#print(result)

#F 
#result = s*2
#print(result)

#4 Write a program that prompts the user 
# for two integers and then prints 

#A The sum 

num1 = int(input("Enter the first integer "))
num2 = int(input("Enter the second integer "))


#sum = num1 + num2
#print("The sum is: ", sum)

#B The difference

#result = num1 - num2
#print("The difference is: ",result )

#C The product 

#result = num1 * num2
#print("The product is39: ", result)

#D The average 

#result = (num1 + num2)/ 2
#print("The average is: ", result)

#E The distance (absolute value of the difference) 

#result = abs(num1 - num2)
#print("The distance between the numbers is", result)

#F The Maximum 

#result = max(num1, num2)
#print("The maximum number is:", result)

#G The minimum 

result = min(num1, num2)
print("The minimum number is:", result)

import math




#x = 2.5
#y = -1.5
#m = 18
#n = 4

#A) print(x + n - (x + n) * y)
#B) print(m // n + m % n)
#C) print(5 * x - n / 5)
#D) print(1 - (1 - (1 - 1 - (1 - n))))
#E) print(math.sqrt (math.sqrt (n)))

#n = 17
#m = 18

#print(n // 10 + n % 10)
#print(m // n + m % n)
#print((m + n) // 2)
#print((m + n) / 2.0)
#print(int(0.5 * (m + n)))
#print(int(round(0.5 * (m+n))))

#s = "Hello"
#t = "World"

#print(len (s) + len(t))
#print(s[1] + s[2])
#print(s[len(s) // 2])
#print(s + t)
#print(t + s)
#print(s * 2)

number1 = int(input("Enter a whole number: "))
number2 = int(input("Enter a whole number: "))

sum = number1 + number2
difference = number1 - number2
product = number1 * number2
avarage = (number1 + number2)/2
distance = math.dist([number1], [number2])
maximum = max(number1, number2)
minimum = min(number1, number2)

#print("The sum is: " + str(sum))
#print("The difference is: " + str(difference))
#print("The product is: " + str(product))
#print("The avarage is: " + str(avarage))
#print("The distance is: " + str(distance))
#print("The maximum is: " + str(maximum))
#print("The minimum is: " + str(minimum))

#print("\nSum = %20d\nDifference = %20d\nProduct = %20d\nAvarage = %20d\nDistance = %20d\nMaximum = %20d\nMinimum = %20d " % (sum, difference, product, avarage, distance, maximum, minimum))

print("%-15s" % "Sum =", number1+number2)
print("%-15s" % "Difference =", number1-number2)
print("%-15s" % "Product =", number1*number2)
print("%-15s" % "Avarage =", (number1+number2)/2)
print("%-15s" % "Distance =", abs(number1-number2))
print("%-15s" % "Max =", max(number1,number2))
print("%-15s" % "Min =", min(number1,number2))


#shortSide = int(input("Write a number: "))
#longSide = int(input("Write a number: "))

#area = shortSide + longSide
#perimeter = 2 * area

#print("Area is: %10dcm\nPerimeter is: %5dcm" % (area, perimeter))

#simpleWord = "Penis"

#print(simpleWord[:2] + "..." + simpleWord[-2:])

#replaceName = simpleWord.replace("n", "...")
#print(replaceName)

#digits = str(12345)

#print(digits[0],digits[1],digits[2],digits[3],digits[4])

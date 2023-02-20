# A

# i = 0
# j = 10
# n = 0 

# linebreaker = "-------------------------------------"

# print(linebreaker)
# print("%5s" % "i", "%5s" % "|", "%5s" % "j", "%5s" % "|", "%5s" % "n",  "%5s" % "|")
# print(linebreaker)
# while i < j : 
#      i = i + 1
#      j = j - 1
#      n = n + 1
#      print(linebreaker)
#      print("%5s" % str(i), "%5s" % "|", "%5s" % str(j), "%5s" % "|", "%5s" % str(n), "%5s" % "|")

#B

# i = 0
# j = 0
# n = 0 

# linebreaker = "-------------------------------------"

# print(linebreaker)
# print("%5s" % "i", "%5s" % "|", "%5s" % "j", "%5s" % "|", "%5s" % "n",  "%5s" % "|")
# print(linebreaker)
# while i < 10 : 
#     i = i + 1
#     n = n + i + j
#     j = j + 1
#     print("%5s" % str(i), "%5s" % "|", "%5s" % str(j), "%5s" % "|", "%5s" % str(n), "%5s" % "|")
#     print(linebreaker)

#C

# i = 10
# j = 0
# n = 0 

# linebreaker = "-------------------------------------"

# print(linebreaker)
# print("%5s" % "i", "%5s" % "|", "%5s" % "j", "%5s" % "|", "%5s" % "n",  "%5s" % "|")
# print(linebreaker)
# while i > 0 : 
#     i = i - 1
#     j = j + 1
#     n = n + i - j
#     print("%5s" % str(i), "%5s" % "|", "%5s" % str(j), "%5s" % "|", "%5s" % str(n), "%5s" % "|")
#     print(linebreaker)

#D

# i = 0
# j = 10
# n = 0 

# linebreaker = "-------------------------------------"

# print(linebreaker)
# print("%5s" % "i", "%5s" % "|", "%5s" % "j", "%5s" % "|", "%5s" % "n",  "%5s" % "|")
# print(linebreaker)
# while i != j : 
#     i = i + 2
#     j = j - 2
#     n = n + 1
#     print("%5s" % str(i), "%5s" % "|", "%5s" % str(j), "%5s" % "|", "%5s" % str(n), "%5s" % "|")
#     print(linebreaker)

# n = int(input("Write a number: "))
# i = 0 
# square = i * i
# while square < n :  
#     print(square)
#     square = i * i
#     i = i + 1
    

# c = 0
# f = 0
# linebreak = "-----------------------------"
# print("%-10s" % "Celsius", "%s" % "Fahrenheit") 

# while c <= 100 : 
#     f = c * (9/5) + 32
#     print("%5s" % str(c), "%5s" % "|", "%5s" % str(f), "%5s" % "|")
#     c = c + 10

#4
# list = [ "Harry"
#         ,"Morgan"
#         , 94
#         , 71
#         , 86
#         , 95 
#         , -1]
# total = 0.0
# count = 2
# print(list[0], list[1])
# while True :
#     if list[count] < 0 :
#         break
    
#     print(list[count])
#     total = total + list[count]
#     count = count + 1
    
# if count > 0 :
#     avarage = total/(count-2)
#     print("%-22s" % "The avarage score is: ", "%.2f" % avarage)
    
# else:
#     avarage = 0

inputStr = input("Write a sentence: ")
count = 0
inputStr = inputStr
# while count < len(inputStr): 
#     if inputStr[count].isupper():
#         print(inputStr[count])
    
#     count = count + 1

# while count < len(inputStr): 
   
#         print(inputStr[count], end= " ")
#         count = count + 2
# new_s = inputStr
# vowels = ["a", "e", "i", "o", "u", "y", "æ", "ø", "å", "A", "E", "I", "O", "U", "Y", "Æ", "Ø", "Å"]
# while count < len(vowels):
#     new_s = new_s.replace(vowels[count], "_")
#     count = count + 1
#     print(count)
# print(new_s)

digit = 0

while count < len(inputStr) :
    if inputStr[count].isdigit():
        digit = digit + 1
    count = count + 1
print("There is:", digit, "digits in this sentence.")

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
    

c = 0
f = c * (9/5) + 32
linebreak = "-----------------------------"
print("%s" % "Celsius", "%3s" % "|", "%s" % "Fahrenheit", "%s" % "|") 

while c <= 100 : 
    f = c * (9/5) + 32
    print("%5s" % str(c), "%5s" % "|", "%7s" % str(f), "%3s" % "|")
    c = c + 10

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


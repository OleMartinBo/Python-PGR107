# #Task1

# print("_________________")
# print("     Task A      ")
# print("_________________ \n")
# lineBreak = "-----------------"
# i = 0
# j = 10
# n = 0
# while i < j :
#     i = i + 1
#     j = j - 1
#     n = n + 1 
#     print("%2s" % str(i), "%2s" % "|", "%2s" % str(j), "%2s" % "|", "%2s" % str(n), "%2s" % "|")
#     print(lineBreak)

# print("_________________")
# print("     Task B      ")
# print("_________________ \n")

# i = 0
# j = 0
# n = 0
# while i < 10 : 
#     i = i + 1
#     n = n + i + j
#     j = j + 1
#     print("%2s" % str(i), "%2s" % "|", "%2s" % str(j), "%2s" % "|", "%2s" % str(n), "%2s" % "|")
#     print(lineBreak)

# print("_________________")
# print("     Task C      ")
# print("_________________ \n")

# i = 10
# j = 0
# n = 0
# while i > 0 : 
#     i = i - 1
#     j = j + 1
#     n = n + i - j
#     print("%2s" % str(i), "%2s" % "|", "%2s" % str(j), "%2s" % "|", "%2s" % str(n), "%2s" % "|")
#     print(lineBreak)


# print("_________________")
# print("     Task D      ")
# print("_________________ \n")

# i = 0
# j = 10
# n = n + 1
# while i !=j :
#     print("%2s" % str(i), "%2s" % "|", "%2s" % str(j), "%2s" % "|", "%2s" % str(n), "%2s" % "|")
#     print(lineBreak)


# print("_________________")
# print("     Task 2      ")
# print("_________________ \n")

# n = int(input("Enter a number: "))
# i = 0
# while i**2 < n:
#     print(i**2, end=' ')
#     i += 1

print("_________________")
print("     Task 3      ")
print("_________________ \n")

c = 0
f = 0 
print("%s" % "|","%5s" % "Celsius", "%6s" % "|", "%7s" % "Fahrenheit", "%4s" % "|")
print("--------------------------------")

while c <= 100 : 
    f = c * (9/5) * 32
    print("%5s" % str(c), "%8s" % "|", "%5s" % str(f), "%5s" % "|")
    c = c + 10
    
import math as m

# x = int(input("Enter value for x: "))
# y = int(input("Enter value for y: "))
# z = int(input("Enter value for z: "))
# n = int(input("Enter value for n: "))
#
# permuation = [[i, j, k] for i in range (n) for j in range(n) for k in range(n)]
# # the above is a list comprehenshion of nested for loops
#
# sortedPermutation = []
#
# for i in permuation:
#     if sum(i) < n:
#         sortedPermutation.append(i)
#
# print(sortedPermutation)

# list1 = [1, 5, 8, 5, 9, 6]
# print(list1)
# list1.sort(reverse=True)
# print(list1)
# print(list1[0])
# print(list[0] < list[0])
#
# for i in list1:
#     if list1[0] < i:
#         print(i)
#     elif list1[1] < i:
#         print(i)
#     else:
#         break
#

# word = "james"
# abcList = ["a", "e", "i", "o", "u"]
# vowels = []
# consonants = []
#
# for letter in word:
#     for letters in abcList:
#         if letter == letters:
#             vowels.append(letter)
#             break
#         elif letter not in consonants:
#             consonants.append(letter)
#             break
#
# print(vowels)
# print(consonants)

# def circleArea():
#     radius = float(input("enter a radius: "))
#     pi = 3.14159265358979
#     area = pi * (radius ** 2)
#     print(f"The area of the circle is {area}.")
#
# circleArea()

# number = int(input("Enter an integer: "))
# result = 0
# remainder = 0
#
# while number != 0:
#     remainder = number % 10
#     result += remainder  #this adds the remainder which is an integer
#     number = int(number / 10)  # this divides the number by 10 and removes the decimal.
#
#     """
#     ex. given int "1234"
#     remainder is 4 which passes to result
#     result = 4
#     int (1234/10) = 123.4 but int removes decimal so
#     number = 123
#     loop runs again
#     remainder is 3 which is added to result
#     result = 7
#     number/10
#     number = 12
#
#     result = 7 + 2 = 9
#     12/10 = 1
#     1 % 10 = .1 = 1
#     result = 9 + 1 = 10
#     number 1/10 = 0.1 but int(.01) = 0
#
#     """
#
# print(f"the sum of digits is: {result}")


# def calc_mini(x, y, op):
#     oper = ["+", "-", "*", "/"]
#     try:
#         if (x > 0) & (y > 0):
#             if op == oper[0]:
#                 print(x + y)
#             elif op == oper[1]:
#                 print(x - y)
#             elif op == oper[2]:
#                 print(x * y)
#             elif op == oper[3]:
#                 print(x / y)
#             else:
#                 print("unknow value")
#         else:
#             print("unknow value")
#     except:
#         print ("unknown value")


# test1 = [116, 105, 117, 121, 101, 101, 116, 105, 105, 105, 105, 116]
# # i decided to make multiple duplicates becuase i wasn't understanding why i works on duplicates.
# # index() returns the first index position but what i forgot is that after the first duplicate
# # is changed to a vowel, the index() will give the index # of the next duplicate.
# # The list is constantly being updated so once 105 gets chagned, it no longer exist in position 1
# def vowel_check(list1):
#     vowel_list = ["a", "e", "i", "o", "u"]
#     for item in list1:
#         for num in range(5):
#             if chr(item) == vowel_list[num]:
#                 list1[list1.index(item)] = chr(item)
#
#     print(list1)
#
# vowel_check(test1)


# text = "Say Hi ASLDKJ"
# swappped_text = ""
# for letter in text: # You can just used the swapcase() method but below is a simple code
#     if letter.islower():
#         swappped_text += letter.upper()
#         # print(letter.upper())
#     elif letter.isupper():
#         swappped_text += letter.lower()
#         # print(letter.lower())
#     elif letter == " ":
#         swappped_text += " "
#         # print(" ")
#
# print(swappped_text)

# text1 = "    This is a string. "
# def split_and_join(line):
#     # write your code here
#     print(f"this is the original input: {line}")
#     line = line.split()   #This creates a list
#     print(f"this is after the split: {line}")
#     line = "-".join(line) #This joins the list with "-"
#     print(f"this is after the join: {line}")
#
# split_and_join(text1)


# def integrate(coefficient, exponent):
#     print(f"{coefficient//exponent + 1}x^{exponent + 1}")

#
# def calculate_tip(amount, rating):
#     tip = 0
#     if rating == "terrible":
#         pritn(tip)
#     elif rating == "poor":
#         tip = m.ceil(amount * .05)
#         print(tip)
#
# calculate_tip(5, "poor")


name = "james"
name1 = [i for i in name]
name1_other = list(name)
name2 = name1[::-1]
name2_reverse = "".join(name2)

name_list = ["j", "a", "m", "e", "s"]
name_reversed = name_list[::-1]
name_join = "".join(name_list)
name_reversed = name_list[::-1]
name_reversed_joined = "".join(name_reversed)

print(name_join)
print(name_reversed_joined)
print(name1)
print(name2)
print(name2_reverse)
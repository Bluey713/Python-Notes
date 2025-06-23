
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


#Trying to create a program that takes a sentence and return the total words and number of repeated words
# sent = "This sentence contains five words"
# repeated_words = "This has eight words and two repeated words"
# word_count = 0
# repeated_count = 0

# list_1 = list(sent.split())
# print(list_1)
# for word in list_1:
#     word_count += 1
# print(word_count)


# list_2 = list(repeated_words.lower().split())
# set_1 = set(list_2)
# print(set_1)
# print(list_2)
# for word in list_2:
#     word_count += 1
#     for i in range(1, len(list_2)):
#         if list_2[i] == word:
#             repeated_count += 1
#         else:
#             continue
#
# print(f"There are {repeated_count} repeated words and a total of {word_count} words")

list_1 = [1, 2, 3]
list_1.popitem() #Doesnt exist for lists. only dictionaries

import math

dict1 = {"say":"hello", 5:"Big 5", "b":True}
# # letters are not keys or values. They must be surrounded by quotes. they must be strings
# dict1["Good"] = "Bye" # since "Good" is not a key, it updates the dictionary with the new pair
# print(dict1)
# # print(dict1.items()) #prints the key values
# # print(dict1.values()) #prints the value items
#
# dict2 = dict(one=1) #one does not need to be a string. It automatically converts it
# # print(dict2)
#
# dict2.update({"one": 2})
# # print(dict2)

# list1 = ["james", "james"]
# dict2 = {"say":"hellow", "say":"hello"} #the first "say" gets overwritten.
# name = "jaaames"
#
# string1 = "The order of the pheonix."
# string_list = string1.lower().split()
# dict_count = {}
#
# for word in string_list:
#     dict_count[word] = dict_count.get(word, 0) + 1
#
# print(dict_count)

# def frequency_in_string():
#     string_input = input("Enter a stentence: ").strip() #input returns a string so no need for str
#     # string_imnput = input("Enter a stentence: ").strip().lower().split() this avoids the need to have the line below
#     string_to_list = string_input.lower().split()
#     word_count = {}
#
#     for word in string_to_list:
#         word_count[word] = word_count.get(word, 0) + 1
#         # this creates the key and value. since their is no current value its set to 0 then plus 1
#     print(f"The result is: {word_count}")
#
# frequency_in_string()

# def frequency_of_letters():
#     string_input = input("Enter a word of sentence to count the instances of each letter: ").strip(" ")
#     letter_count = dict()
#     for letter in string_input:
#         letter_count[letter] = letter_count.get(letter, 0) +1
#
#     print(letter_count)
#
# frequency_of_letters()


# def count_letters():
#     letter_input = input("enter letters, words, or a sentence: ").strip().replace(" ", "")
#     letter_dict = {}
#     try:
#         for letter in letter_input:
#             # if letter == " ":   #Used this to get rid of spaces but you can just use .replace(" ", "")
#             #     continue
#             letter_dict[letter] = letter_dict.get(letter, 0) + 1
#         # print(letter_dict)
#         sorted_dict = sorted(letter_dict.keys()) #sorted automatically sorts by keys so .keys() is unnecessary. THIS IS A LIST
#         # print(sorted_dict)
#         # for key_value in letter_dict:
#         #     print(key_value, letter_dict.get(key_value))
#         #better for loop without "redudancy of .get is below
#         for key_value in sorted_dict:
#             print(key_value, letter_dict[key_value])
#     except:
#         print("thers something wrong with the last for loop")
#
# count_letters()


#Below im testing if the sorted function works like in lists. This functions does not just reference the old dict.
# dict2 = {"a": 1, "c": 3, "b": 2, "g": 5}
# dict3 = sorted(dict2)
# dict4 = sorted(dict2.keys())
# dict5 = sorted(dict2.values())
#
# print(dict3)
# print(dict4)
# print(dict5)
# print(dict2) #dict2 never changes after its sorted.

# stock = {
#             'football': 4,
#             'boardgame': 10,
#             'leggos': 1,
#             'doll': 5 }
# this was my inital code
# for item in stock:
#     if item == merch:
#         if stock[item] >= n:
#             return True
#         else:
#             return False
#     else:
#         return False

# def fillable(stock, merch, n):
#     try:
#         if merch in stock.keys():
#             for item in stock:
#                 if item == merch:
#                     if stock[item] >= n:
#                         return True
#                         break
#                     else:
#                         return False
#                 else:
#                     continue
#         else:
#             return False
#     except:
#         print("Somethings wrong with the code!")

#Testing nested dictionaires for mini project.
nest_dict = {"Utilities": {"Gas":0, "Electricity": 0, "Water": 0},
             "Food": {"Groceries": 0, "Fast Food": 0}
             }

print(nest_dict.values())
nest_dict["Gas"] = nest_dict.get("Gas", 0) + 10
print(nest_dict.values())
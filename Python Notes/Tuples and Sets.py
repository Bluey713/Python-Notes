# tuple_1 =("Hello",)
#
# print(type(tuple_1))
# print("hello" in tuple_1)
#
# name = "James"
# string_to_tuple = tuple(name)   #this is the sampe as tuple("James") each letter gets split
# print(string_to_tuple)
# name_2 = "Potter"
# concat_name = tuple(name + name_2)
# print(concat_name)
# name_tup1 = ("James",)
# name_tup2 = ("Potter",)
# concat_tup = name_tup1 + name_tup2
# print(concat_tup)
# #nested tuples
# nest1 = ("James", "Lily")   #the comma at the end is only necessary if one single elemetn
# nest2 = ("Hermione", "Ron")
# nested_tup = (nest1, nest2)
# print(nested_tup)
# print(nest1[0])
# num_tup = ("a", "c", "b")
# print(sorted(num_tup))
#
#
# tup_in_pairs = (("sum","add"), ("sub", "minus"))
# dict_from_tup = dict(tup_in_pairs)  #create a dictionary from a tuple
# print(dict_from_tup)
# print(dict_from_tup["sum"]) #call a key from the newly created dict from a tuple
# dict_to_tup = dict_from_tup.items() #creates a tuple from a dictionary
# print(dict_to_tup)
#
# number_tup = (1, 2, 3, 4, 5)
# print(number_tup)

# user_tup = ()
# user_num = int(input("Enter the amount of integers you want to add to the tuple: "))
# for i in range(user_num):
#     tuple_add = tuple(int(input("Enter the integer you want to add to the tuple: ")))
#     user_tup += tuple_add
#
# print(user_tup)

# #Sets
#
# set_1 = {} #This creates a dictionary
# print(type(set_1))
#
# set_2 = set()   #This is an empty set
# print(type(set_2))
#
# basket = {"orange", "apple", "pear", "banana"}
# #membership testing
# print("apple" in basket)    #prints boolean True
# #set containg NO duplicates so:
# words = set("abracadabra") #similar to the tupple function, it takes an iterable sand splits the iterable to individual elements
# print(words)
# words.add("a")
# print(words)

words_2 = {"This was written as a set"}
print(words_2)
words_3 = "This was written as a regular string"
words_4 = words_3.split()
words_5 = sorted(list(set(words_4)))
print(words_3)
print(words_4)
print(words_5)

tuple_looping = ("a", "b", "c", "d")
# for i in range(0, len(tuple_looping), 2):
#     print(tuple_looping[i])

tuple_looping2 = ("b", "a", "c", "d")
print(tuple_looping < tuple_looping2)
tuple_nums = (1, 2, 3, 4, 5, 6, 7)
print(tuple_nums[1:-1]) #indexin returns a tuple of the specified indices


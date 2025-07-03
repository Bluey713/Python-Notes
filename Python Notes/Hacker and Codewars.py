#creat a function that sums the points based on the given values
# def alphabet_war(fight):
#     left_values = {"w": 4, "p": 3, "b": 2, "s": 1}
#     left_score = 0
#     right_values = {"m": 4, "q": 3, "d": 2, "z": 1}
#     right_score = 0
#
#     for letter in fight:
#         # if letter in left_values.keys():
#         #     left_score += left_values[letter]
#         # elif letter in right_values.keys():
#         #     right_score += right_values[letter]
#         #The above 4 lines are my initial code
#         #I saw the below 2 lines to make my code shorter which gets rid of the if statement.
#         left_score += left_values.get(letter, 0)
#         right_score += right_values.get(letter, 0)
#
#     if left_score > right_score:
#         print("Left side wins!")
#     elif right_score > left_score:
#         print("Right side wins!")
#     else:
#         print("Let's fight again!")
#
# alphabet_war("pqd")

# # printer errors
# def printer_error(s):
#     colors = "abcdefghijklm"
#     total_count = 0
#     error_count = 0
#
#     for letter in s:
#         if letter in colors:
#             total_count += 1
#         else:
#             error_count += 1
#             total_count += 1
#             continue
#
#     return f"{error_count}/{total_count}"

# #return the highes and lowest number
# #numbers will be a string of space separated numbers
# nums = "5 6 9 3 4 6"
#
# def high_and_low(numbers):
#     num_list = [int(x) for x in numbers.split()]
#     return f"{max(num_list)} {min(num_list)}"
#
# high_and_low(nums)

# def am_I_afraid(day,num):
#     if day == "Monday" and num == 12:
#         return True
#     elif day == "Tuesday" and num >95:
#         return True
#     elif day == "Wednesday" and num == 34:
#         return True
#     elif day == "Thurdsay" and num == 0:
#         return True
#     elif day == "Friday" and (num % 2) == 0:
#         return True
#     elif day == "Saturday" and num == 56:
#         return True
#     elif day == "Sunday" and (num == 666 or num ==-666):
#         return True
#     else:
#         return False

# #takes in an array and an integer. find the occurances of the integer in the array and return a list of the indexes where it occurs.
# def find_all(array, n):
#     count = 0
#     occur_list = []
#     for num in range(len(array)):
#         if array[num] == n:
#             count += 1
#             occur_list.append(num)  #if nothing gets appended, it remains an empty list
#
#     return occur_list

#Take in a string and return the string reversed including the spaces.
# def reverse_words(text):
#     list_1 = list(text.split(" "))
#     print(list_1)
#     list_2 = []
#
#     for each_word in list_1:
#         print(each_word[::-1])
#         list_2.append(each_word[::-1])
#     #
#     #
#     # return " ".join(list_2)
#     print(" ".join(list_2))
#This was my first attempt

# def reverse_words(text):
#     list_1 = list(text.split(" "))
#     list_2 = [x[::-1] for x in list_1]
#     # list_2 = [x[::-1] for x in text.split(" ")] idea from codewars solution
#
#     return " ".join(list_2)
# #This was my final solution. To shorten it i could have done [x[::-1] for x in text.split(" ")]
#
# sample = "This  is  a  sample"
# reverse_words(sample)

# def case_sensitive(s):
#     new_list = [letter for letter in s if letter.isupper()]
#     if len(new_list) > 0:
#         return [False, new_list]
#     else:
#         return [True, new_list]
#
# case_sensitive("codewARs")

# def scoreboard(st):
#     convert = {
#         "nil": 0,
#         "one": 1,
#         "two": 2,
#         "three": 3,
#         "four": 4,
#         "five": 5,
#         "six": 6,
#         "seven": 7,
#         "eight": 8,
#         "nine": 9
#     }
#     score = [convert[num] for num in st.split() if num in convert]
#
#     print(score)
# st1 = "the score is six five"
# scoreboard(st1)

from math import ceil
def sillycase(silly):
    num = ceil(len(silly)/2)
    lower_case = [letter.lower() for letter in silly[:num]]
    upper_case = [letter.upper() for letter in silly[num:]]
    #refactored code to the above 2 lines from the bottom 5 lines
    # change_case = ""
    # for letter in silly[:num]:
    #     change_case += letter.lower()
    # for letter in silly[num:]:
    #     change_case += letter.upper()
    #return silly[:half].lower() + silly[half:].upper() per CodeWars
    print("".join(lower_case + upper_case))

sillycase("briian")






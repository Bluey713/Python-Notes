#if the inputs are unclear in a program run the following
# import sys
#
# for line in sys.stdin:
#     print(f"Received line: {line.strip()}")
#The above will print if the inputs are one input or multiple
#so the day 6 inputs were 3 separate inputs, so I need to use 3 inputs, one for int and n for each nth string


#Day 6 of 30 days of code
#creat a program that takes in an int of how many words will be entered and for
# each word, print the even and odd letter as a space separated string
# ex. 2, hacker, rank prints hce akr rn ak
# n = int(input())
# for i in range(n):
#     s = input()
#     print(f"{s[::2]} {s[1::2]}")


# #Day 7
# # n = int(input().strip())
#
# arr = list(map(int, input().rstrip().split()))
#
# # new_string = ""
# # for i in arr[::-1]:
# #     new_string += str(i) + " "
# #
# # print(new_string.strip())
#
# #easier method
# arr.reverse()
# print(*arr) #an asterisk unpacks the list to a string


#Day 8. create a contact list with a dictionary

#if name not in dictionary print "not found"
#so use dict.get("name", "Not found")?

n = int(input("enter #: ")) #takes in number of lines to be added
name_phone_pairs = {}

for i in range(n):
    contact = list(input("enter contact pair: ").lower().split())
    name_phone_pairs[contact[0]] = contact[1]

while True:
    try:
        name = input("which contact would you like to search: ").lower().strip()
        if name in name_phone_pairs.keys():
            print(f"{name}={name_phone_pairs.get[name]}")
        else:
            print("Not found")
    except EOFError:
        break
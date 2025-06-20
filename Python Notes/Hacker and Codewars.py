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

# printer errors
def printer_error(s):
    colors = "abcdefghijklm"
    total_count = 0
    error_count = 0

    for letter in s:
        if letter in colors:
            total_count += 1
        else:
            error_count += 1
            total_count += 1
            continue

    return f"{error_count}/{total_count}"

import time, random, copy


# def add_test():
#     print("You have chosen the add function.")
#     num_1 = int(input("Enter the first number: "))
#     num_2 = int(input("Enter the second number: "))
#     return print("The resutl is " +  str(num_1 + num_2))
#
# def sub_test():
#     print("You have chosen the sub function.")
#     num_1 = int(input("Enter the first number: "))
#     num_2 = int(input("Enter the second number: "))
#     return print("The result is " +  str(num_1 - num_2))
#
# def div_test():
#     print("You have chosen the div function.")
#     num_1 = int(input("Enter the first number: "))
#     num_2 = int(input("Enter the second number: "))
#     return print("The result is " +  str(num_1 / num_2))
#
# def mult_test():
#     print("You have chosen the mult function.")
#     num_1 = int(input("Enter the first number: "))
#     num_2 = int(input("Enter the second number: "))
#     return print("The result is " +  str(num_1 * num_2))
#
#
# run = "yes"
#
# while run == "yes":
#
#     choice = (input("Choose the calculator function you want to use. Type add/sub/div/mult: ").lower())
#
#     if choice == "add":
#         add_test()
#         run = input("Would you like to use another function? yes/no ").lower()
#
#     elif choice == "sub":
#         sub_test()
#         run = input("Would you like to use another function? yes/no ").lower()
#
#     elif choice == "div":
#         div_test()
#         run = input("Would you like to use another function? yes/no ").lower()
#
#     elif choice == "mult":
#         mult_test()
#         run = input("Would you like to use another function? yes/no ").lower()
#
#     else:
#         print("The choice was invalid. Goodbye!")
#         break
#
#     print("Thanks for using my calculator. Goodbye!")
import re


#For loops


# #the "i" can be any variable. its a placeholder variable that takes in anything from the actual variable
#
# sample = "Jose"
#
# for i in sample:
#     print(i)

#Leap year calculator
# year = int(input("Enter a year to check if it is a leap year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year.")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is not a leap year")
# else:
#     print(f"{year} is not a leap year")

# def two_var():
#     first = input("enter the first variable: ")
#     second = input("enter the second variable: ")
#     return first, second
#
# def two_test():
#     one, two = two_var() #this takes the iput from the fuunction which are returned in order
#                         # and pluges them into var "one" and "two" in that order.
#                         # If you switch the order in the return statement, they will switch.
#     print(f"the first var input is {one} and the second is {two}")
#
# two_test()

#Tip calculator

# def bill_amount():
#     while True:
#         amount = input("Enter the bill amount: ")
#         try:
#             amount_converted = round(float(amount), 2)
#             if amount_converted >= 0:
#                 print(f"The amount entered is ${amount_converted}")
#                 return amount_converted
#             else:
#                 print("Please enter a positive amount.")
#         except ValueError:
#             print("Please enter a number not letters")
#
# def tip_amount():
#     while True:
#         amount = input("Enter the tip amount: ")
#         try:
#             amount_converted = round(float(amount), 2)
#             if amount_converted >= 0:
#                 print(f"The tip entered is ${amount_converted}")
#                 return amount_converted
#             else:
#                 print("Please enter a positive amount.")
#         except ValueError:
#             print("Please enter a number not letters")
#
#
# def total_calculation():
#     bill, tip_percent = bill_amount(), tip_amount()
#     tip = bill * tip_percent
#     total = bill + tip
#     rounded_total = round(total, 2)
#     print(f"The total bill is ${bill}")
#     print(f"The total tip percentage is {tip_percent}")
#     print(f"The total tip is ${tip}")
#     print("-" * 20)
#     print(f"The total is ${rounded_total}")
#
# # Random testing
#
# alphabet = ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
#
# def charachter_length():
#     #trying to create a functions that takes in a string, not numbers, and outputs how many characters in it.
#     while True:
#         sample = input("enter a word or string of words: ")
#         try:
#             if sample in alphabet:
#
#                 return print(f"The word has {len(sample)} characters.")
#
#
#             else:
#                 print(f"Please enter a string with only letters in the alphabet.")
#
#         except ValueError:   #ValueError is the error thrown when you enter a letter into an int or number into str
#             print("Please enter a word not numbers")
#
#
# charachter_length()

# ranGuess = random.randint(1, 20)


# for i in range(1, 7): # This limits the range to start at 1 and stop a 6(7-1). see commented block below
#     # for i in range(1, 7):
#     #     print(i)
#
#     userGuess = int(input("Take a guess: "))
#
#     if userGuess < ranGuess:
#         print(f"Your guess is too low, try again. You have {6-i} guesses left")
#     elif userGuess > ranGuess:
#         print(f"Your guess is too high, try again. You have {6-i} guesses left")
#     else:
#         break
#
# if userGuess == ranGuess:
#     print(f"You got it! It took you {i} guesse(s)!")

# indent = 0
# indentIncreasing = True
#
# try:
#     while True:
#         print(" " * indent, end="") # the "end=' '" is the append function to the print statement
#         print("********")           # without it, this print statement would print on a new line /n and the previous line would be just a blank line
#         time.sleep(0.1)             # This adds a delay to printing the new line to a tenth of a second
#         #
#         if indentIncreasing:
#             indent += 1
#             if indent == 20:
#                 indentIncreasing = False
#
#         else:
#             indent -= 1
#             if indent == 0:
#                 indentIncreasing = True
#
# except KeyboardInterrupt:
#     sys.exit()

# def collatz(number):     # works but the try and except dont. since im already converting the input to an int it throws an error when its a string
#     print(number)
#
#     try:
#         while number != 1:
#
#             if number % 2 == 0:
#                 print(number // 2)
#                 number = (number // 2)
#
#             else:
#                 print(3 * number + 1)
#                 number = (3 * number +1)
#
#     except ValueError:
#         sys.exit()
# userInt = int(input("Enter any integer greater than 1: "))
# collatz(userInt)

WIDTH = 60
HEIGHT = 20

nextCells = []

for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append("#")
        else:
            column.append(" ")
    nextCells.append(column)

while True:
    print("\n\n\n\n\n")
    currentCells = copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end=" ")
        print()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1 ) % HEIGHT

            numNeighbors = 0
            if  currentCells[leftCoord][aboveCoord] == "#":
                numNeighbors += 1
            if currentCells[x][aboveCoord] == "#":
                numNeighbors += 1
            if currentCells[rightCoord][aboveCoord] == "#":
                numNeighbors += 1
            if currentCells[leftCoord][y] == "#":
                numNeighbors +=1
            if currentCells[leftCoord][belowCoord] == "#":
                numNeighbors += 1
            if currentCells[x][belowCoord] == "#":
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == "#":
                numNeighbors += 1

            if currentCells[x][y] == "#" and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = "#"
            elif currentCells[x][y] == " " and numNeighbors == 3:
                nextCells[x][y] == " "
            else:
                nextCells[x][y] == " "
    time.sleep(1)









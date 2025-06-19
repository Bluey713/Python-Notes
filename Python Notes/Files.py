# new_file = open("test.txt","x") #opens the file. See doc for the access code
# new_file.close() #you should always close the file or else you can't access the file

#Me testing adding text to a file
# try:
#     # new_file2 = open("test.txt", "r+")  # 1 ran this line then commented out to write additional lines
#     new_file2 = open("test.txt", "a")   # 2 then ran this
#     try:
#         # new_file2.write("Line 1: Hello World!") # 1 ran the program with this line then created line 2
#         # new_file2.write("Line 2: Does not include the new line character before or after this string")  # 2 then ran this
#         # new_file2.write("Line 3: Testing the new line character "
#         #                 "\n Line 4: does this work as you thought?")    # 3 this didnt work as expected but 4 did.
#         new_file2.write("\nLine 3: testing for the second time. "
#                         "\nLine 4: does this work as you thought?") #4 this adds two new lines to the text file as expected
#     finally:
#         new_file2.close()
# except IOError:
#     print("Something went wrong!")

# #This following takes the text file and prints each line with a for loop
# new_file2 = open("test.txt", "r")
# for each_line in new_file2:
#     print(each_line) #This prints a new line followd by a blank line sine \n is invisible. to remove add end=""
# new_file2.close()  #ALWAYS remember to CLOSE THE FILE!!!!!

#opening and reading a file using the "with" statement. This opens and closes the files even if exceptions are thrown
with open("test.txt") as new_file3: #"as" assigns the variable to new_file3
    for each_line in new_file3:
        print(each_line, end="")    #using the with statment, there is no need to run the close() method
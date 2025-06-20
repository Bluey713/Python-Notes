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

# #opening and reading a file using the "with" statement. This opens and closes the files even if exceptions are thrown
# with open("test.txt") as new_file3: #"as" assigns the variable to new_file3
#     for each_line in new_file3:
#         print(each_line, end="")    #using the with statment, there is no need to run the close() method

# #opening multiple files and adding to the file
# with open("test.txt") as in_file, open("testcopy.txt", "w") as out_file:    #opens two files under different variables(file handlers)
#     for each_line in in_file:
#         out_file.write(each_line)   #copies each line in test.txt into testcopy.txt.

# #Testing methods
# with open("testcopy.txt") as file_handler:
#     # print(file_handler.read(10))    #prints the first 10 characters
#     # print(file_handler.read(), end="")  #prints out all charaters or all lines as if running a for loop
#     #^^ question i have is, what happens if you pass .write(file_handler.read(), end="")? will it make a copy like in the previous block?
#     # print(file_handler.readline())    #prints the first line
#     # print(file_handler.readline())    #if two readline are ran consecutively, they add a new blank line in between.
#     print(file_handler.readline(), end="")    #This gets rid of the blank line
#     print(file_handler.readline())
#     # print(file_handler.readlines())   #prints all lines as a list. each element is a line

#program to take in a text file, read it and have each word reversed.


# test = ("This is line 1"
#         "\nThis is line 2")
#
# for each_word in test:
#     string_list += each_word
#
# print(string_list)
#
# for each_word in string_list:
#     reversed_list = " ".join(string_list[::-1])
# print(reversed_list)

with open("Reverse Text.txt", "w+") as reverse_file:
    reversed_list = []
    joined_list = []
    reverse_file.write("This is line one"
                       "\nThis is line two")
    reverse_file.seek(0)
    for each_line in reverse_file:
        string_list = each_line.strip().split()
        for each_word in string_list:
            reversed_list.append(each_word[::-1])
    # print(string_list)
    # # for each_word in string_list:
    #
    joined_list = " ".join(reversed_list)
    print(joined_list)
    reverse_file.seek(0)
    reverse_file.writelines(joined_list)




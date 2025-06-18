#I understund the basics of functions but never understood args and kwargs
def testing_keyword(test3, test1="name", test2="last name"):
    print(test3)
    print(test1)
    print(test2)

testing_keyword(1000)
testing_keyword(test3="James")
testing_keyword(test3 = "New name", test1="This is the new string")


# class Mobile:
#     #You have to initialize the object first
#     def __init__(self):
#         print("This message is from Constructor Method")
#
#     #The two methods are below
#     def receive_message(self):
#         print("Receive message using Mobile")
#
#     def send_message(self):
#         print("Send message using Mobile")
#
# def main():
#     nokia = Mobile()
#     nokia.receive_message()
#     nokia.send_message()
#
# main()

# class Mobile:
#     #You have to initialize the object first
#     def __init__(self, name):
#         self.name = name    #self acts like the object name. its the same as nokia.name = name
#
#     #The two methods are below
#     def receive_message(self):
#         print(f"Receive message using {self.name} Mobile")
#
#     def send_message(self):
#         print(f"Send message using {self.name} Mobile")
#
# def main():
#     nokia = Mobile("Nokia") #now you have to give an argument since the init def has one parameter(beside self)
#     nokia.receive_message()
#     nokia.send_message()
#
# main()
# import math
#
# class ArcLength():
#     # def __init__(self):     #here were not running additional parameters only creating the placehodler for data attributes
#     #     self.radius = 0
#     #     self.angle = 0
#     def __init__(self, radius, angle):  #This now takes two parameters which will need to be given when the variable is initialized
#         self.radius = radius            #This makes the self.radius take its value from the argument given when the variable = ClassName
#         self.angle = angle              #idk if this way is better or the previous method
#                                         #data attributes should be maintained in the init function and is a good practice to not introduce more after this
#
#     def calculate_arc_length(self):
#         result = 2 * math.pi * self.radius * (self.angle / 360)
#         print(f"Angle is {self.angle}")
#         print(f"Radius is {self.radius}")
#         print(f"Length of an Arc is {result}")
#
# def main(): #Created a function to run it all in one go like the previous example.
#     al = ArcLength(9, 75)
#     al.calculate_arc_length()
#
# main()

# import math
#
# class ArcLength():
#     def __init__(self):     #here were not running additional parameters only creating the placehodler for data attributes
#         self.radius = 0     #per the book these are initialized when the al = ArcLength is run but is not true since al.radius doesnt print
#         self.angle = 0
#
#     def calculate_arc_length(self):
#         result = 2 * math.pi * self.radius * (self.angle / 360)
#         print(f"Angle is {self.angle}")
#         print(f"Radius is {self.radius}")
#         print(f"Length of an Arc is {result}")
#
#
# al = ArcLength
# # al.radius = 1
# print(al.radius)

# class Birds():
#     def __init__(self, type):   #has one paramenter required when
#         self.type = type
#
#     def flying_bird(self):
#         """Prints if this is a flying bird or not."""
#         print(f"{self.type} is a flying bird.")
#
#     def non_flying_bird(self):
#         print(f"{self.type} is the national bird of Australia")
#
# def main():
#     vulture = Birds("Griffon Vulture")
#     crane = Birds("Common Crane")
#     emu = Birds("Emu")
#     vulture.flying_bird()
#     crane.flying_bird()
#     emu.non_flying_bird()
#     print(vulture.type) #me testing what it will print. prints the initial argument passed on the class
#
# main()

class BankAccount():
    def __init__(self, name):
        self.name = name    #again here, were are setting any new varialbe's "self" to be equle to the name argument given.
        self.balance = 0.0  #here we initialize the new bank balance at 0.0 float. we would need a parameter if the customer transfers money in

    def show_balance(self):
        print(f"{self.name} has a balance of {self.balance} dollars")

    def withdraw_money(self, amount):
        if amount > self.balance:
            print("You don't have the sufficient funds in your account.")
        else:
            self.balance -= amount
            print(f"{self.name} has withdrawn an amount of {amount} dollars and the new balance is {self.balance}")

    def deposit_money(self, amount):
        self.balance += amount
        print(f"{self.name} has deposited {amount} dollars and the total balance is {self.balance}")

def main():
    savings_account = BankAccount("Olivia")
    savings_account.deposit_money(1000)
    savings_account.show_balance()
    savings_account.withdraw_money(500)
    savings_account.withdraw_money(499)
    savings_account.withdraw_money(2)
    message = savings_account.balance   #This shows that you can create a new variable and have it equal the object and method
    print(message)

main()
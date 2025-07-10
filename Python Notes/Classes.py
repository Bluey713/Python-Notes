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

# class BankAccount():
#     def __init__(self, name):
#         self.name = name    #again here, were are setting any new varialbe's "self" to be equle to the name argument given.
#         self.balance = 0.0  #here we initialize the new bank balance at 0.0 float. we would need a parameter if the customer transfers money in
#
#     def show_balance(self):
#         print(f"{self.name} has a balance of {self.balance} dollars")
#
#     def withdraw_money(self, amount):
#         if amount > self.balance:
#             print("You don't have the sufficient funds in your account.")
#         else:
#             self.balance -= amount
#             print(f"{self.name} has withdrawn an amount of {amount} dollars and the new balance is {self.balance}")
#
#     def deposit_money(self, amount):
#         self.balance += amount
#         print(f"{self.name} has deposited {amount} dollars and the total balance is {self.balance}")
#
# def main():
#     savings_account = BankAccount("Olivia")
#     savings_account.deposit_money(1000)
#     savings_account.show_balance()
#     savings_account.withdraw_money(500)
#     savings_account.withdraw_money(499)
#     savings_account.withdraw_money(2)
#     message = savings_account.balance   #This shows that you can create a new variable and have it equal the object and method
#     print(message)
#
# main()

# #Testing default parameters
# class Dog():
#     def __init__(self, breed="German Shepherd", color="Tan Black"):
#         self.breed = breed
#         self.color = color
#
#     def dog_breed(self):
#         print(f"Dog breed is {self.breed}")
#
#     def dog_color(self):
#         print(f"Dog color is {self.color}")
#
# def main():
#     babloo = Dog()  #not giving the dog breed or color so it will default to the default value of german shepherd and tan black.
#     babloo.dog_breed()
#     babloo.dog_color()
#     lucky = Dog("Matlepom", "Tan")  #I added these to show that you can enter your own arguments
#     lucky.dog_breed()
#     lucky.dog_color()
#
# main()

# #passing an object as an argument (here singer is the object that was initialized into the Track class)
# class Track:
#     def __init__(self, song, artist):
#         self.song = song
#         self.artist = artist
#         #1 Here we are creating a class that will initialize the object to contain object.song and object.artist
#
# def print_track(vocalist):
#     print(f"Song is {vocalist.song}")   #2 this function takes in a parameter which later we see will be singer. since vocalist is just a placeholder the real var = singer
#     print(f"Artist is {vocalist.artist}")
#
# singer = Track("Family Ties", "Drake")  #1 We initialize the object "singer" which now has two data attributes, song = family ties, artist = drake
#
# print_track(singer) #3 here we just run the functions which prints singer.song and singer.artist since "vocalist" = singer
# #This works as long as we know the object has these methods(data attributes) but what if we didn't? When would we use this?
#
# print(isinstance(singer, Track))

# class Time:
#     def __init__(self, hours: int, minutes: int, seconds: int) -> None:
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def add_time(self, duration) -> None:   #This needs the duration parameter to access the data attributes of the second object
#         opera_hours = self.hours + duration.hours   #here we access the hours attribute of the second object.
#         opera_minutes = self.minutes + duration.minutes
#         opera_seconds = self.seconds + duration.seconds
#
#         while opera_seconds >= 60:  #Seconds need to by less than 60 seconds or else we need subtract 60 seconds to add a minute to minutes
#             opera_seconds -= 60
#             opera_minutes += 1
#
#         while opera_minutes >= 60:  #same here, minutes need to be less than 60 minutes.
#             opera_minutes -= 60
#             opera_hours += 1
#
#         print(f"The total time is {opera_hours}:{opera_minutes}:{opera_seconds}")
#
# def calc_time():
#     opera_start = Time(10, 30, 30)
#     opera_duration = Time(2, 45, 50)
#     opera_start.add_time(opera_duration)
#
# calc_time()

# #Program to show class variable and instance variables.
# class Dog:
#     kind = "canine"     #This is a class variable or shared variable.
#     def __init__(self, name: str):
#         self.dog_name = name    #this is an instance variable or a unique variable to each object instantiated with this class.
#
# d = Dog("Fido")
# e = Dog("Buddy")
# print(f"Value for shared variable or class variable 'kind' is {d.kind}")
# print(f"Value for unique variable or instance variable 'dog_name' is {d.dog_name}")

# # Program to demonstrate the difference between abstraction and encapsulation.
# class foo:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
# #The class is the encapsulation and the method is the abstraction.
# foo_object = foo(3, 4)
# foo_object.add()

# #Inheritance
# class Test(object): #all classes are derived or "subclasses" of the class "object"
#     pass
# class Test1: #This is the same as above since it inherits properties of the class "object" but this is shorthand.
#     pass

#Demo of base and derived class relationship
class FootBall:
    def __init__(self, country: str, division: str, no_of_times: int):
        self.country = country
        self.division = division
        self.no_of_times = no_of_times

    def fifa(self):
        print(f"{self.country} national football team is placed in '{self.no_of_times}' FIFA division")

class WorldChampions(FootBall): #This now inherits everything "Football". That's why we dont run the init def.
    def world_championship(self):
        print(f"{self.country} national football team is {self.no_of_times} times world champions")

def main():
    germany = WorldChampions("Germany", "UEFA", 4)
    germany.fifa()  #This is a method in the "FootBall" class but the worldChamp class inherited this as well
    germany.world_championship()

main()



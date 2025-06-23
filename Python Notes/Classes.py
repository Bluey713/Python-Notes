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
import math

class ArcLength():
    # def __init__(self):     #here were not running additional parameters only creating the placehodler for data attributes
    #     self.radius = 0
    #     self.angle = 0
    def __init__(self, radius, angle):  #This now takes two parameters which will need to be given when the variable is initialized
        self.radius = radius            #This makes the self.radius take its value from the argument given when the variable = ClassName
        self.angle = angle              #idk if this way is better or the previous method

    def calculate_arc_length(self):
        result = 2 * math.pi * self.radius * (self.angle / 360)
        print(f"Angle is {self.angle}")
        print(f"Radius is {self.radius}")
        print(f"Length of an Arc is {result}")


def main():
    al = ArcLength(9, 75)
    al.calculate_arc_length()

main()
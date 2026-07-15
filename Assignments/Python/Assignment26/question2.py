#Write a Python program to implement a class named Circle with the following requirements:

#The class should contain three instance variables: Radius, Area, and Circumference.
#The class should contain one class variable named PI, initialized to 3.14.
#Define a constructor (__init__) that initializes all instance variables to 0.0.
#Implement the following instance methods:
#Accept() – accepts the radius of the circle from the user.
#CalculateArea() – calculates the area of the circle and stores it in the Area variable.
#CalculateCircumference() – calculates the circumference of the circle and stores it in the Circumference variable.
#Display() – displays the values of Radius, Area, and Circumference.
#Create multiple objects of the Circle class and invoke all the instance methods for each object.

class Circle:

    PI = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def accept(self):
        self.radius = int(input("Enter a radius :"))

    def calculateArea(self):
        self.area = Circle.PI * self.radius * self.radius

    def calculateCircumference(self):
        self.circumference = 2 * Circle.PI * self.radius

    def display(self):
        print("Value of Radius is :", self.radius)
        print("Value of Area is :", self.area)
        print("Value of Circumference is :", self.circumference)

cobj = Circle()
cobj.accept()
cobj.calculateArea()
cobj.calculateCircumference()
cobj.display()

cobj2 = Circle()
cobj.accept()
cobj.calculateArea()
cobj.calculateCircumference()
cobj.display()

    
#Write a Python program to implement a class named Arithmetic with the following characteristics:

#The class should contain two instance variables: Value1 and Value2.
#Define a constructor (__init__) that initializes all instance variables to 0.
##Implement the following instance methods:
#Accept() – accepts values for Value1 and Value2 from the user.
#Addition() – returns the addition of Value1 and Value2.
#Subtraction() – returns the subtraction of Value1 and Value2.
#Multiplication() – returns the multiplication of Value1 and Value2.
#Division() – returns the division of Value1 and Value2 (handle division by zero properly).
#Create multiple objects of the Arithmetic class and invoke all the instance methods.

class Arithmatic:

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def accept(self):
        self.value1 = int(input("Enter a first value : "))
        self.value2 = int(input("Enter a second value : "))

    def addition(self):
        print("Addition is : ", self.value1 + self.value2)

    def substraction(self):
        print("Substraction is : ", self.value1 - self.value2)

    def multiplication(self):
        print("Multiplication is : ", self.value1 * self.value2)

    def division(self):
        print("Division is : ", self.value1 / self.value2)

aobj1 = Arithmatic()
aobj2 = Arithmatic()

aobj1.accept()
aobj1.addition()
aobj1.substraction()
aobj1.multiplication()
aobj1.division()

aobj2.accept()
aobj2.addition()
aobj2.substraction()
aobj2.multiplication()
aobj2.division()
    


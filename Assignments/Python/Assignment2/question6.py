#Write a program that accepts two number from user and prints their:
#Addition
#Substraction
#Multiplication
#Division

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition: ", num1 + num2)
print("Subtraction: ", num1 - num2)
print("Multiplication: ", num1 * num2)
if num2 != 0:
    print("Division: ", num1 / num2)
else:    
    print("Division: Cannot divide by zero")
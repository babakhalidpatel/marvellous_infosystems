Write a Python program to implement a class named BankAccount with the following requirements:

The class should contain two instance variables:
Name (Account holder name)
Amount (Account balance)
The class should contain one class variable:
ROI (Rate of Interest), initialized to 10.5
Define a constructor (__init__) that accepts Name and initial Amount.
Implement the following instance methods:
Display() – displays the account holder name and current balance.

Deposit() – accepts an amount from the user and adds it to the balance.
Withdraw() – accepts an amount from the user and subtracts it from the balance.
(Ensure withdrawal is allowed only if sufficient balance exists.)
CalculateInterest() – calculates and returns interest using the formula:
Interest = (Amount * ROI) / 100
Create multiple objects and demonstrate all methods.
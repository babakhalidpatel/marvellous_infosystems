# Write a Python program to implement a class named BankAccount with the following requirements:
# The class should contain two instance variables:
# Name (Account holder name)
# Amount (Account balance)
# The class should contain one class variable:
# ROI (Rate of Interest), initialized to 10.5
# Define a constructor (_init_) that accepts Name and initial Amount.
# Implement the following instance methods:
# Display() - displays account holder name and current balance.
# Deposit() - accepts an amount from the user and adds it to the balance.
# Withdraw() - accepts an amount from the user and subtracts it from the balance.
# (Ensure withdrawal is allowed only if sufficient balance exists.)
# CalculateInterest() - calculates and returns interest using the formula:Interest = (Amount * ROI) / 100
# Create multiple objects and demonstrate all methods.


class BankAccount:
    ROI = 10.5
    def _init_(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount


    def Display(self):
     print("Account holder name is :",self.Name,"And Current Balance is :",self.Amount)


    def Deposite(self):
        amt = int(input("Deposite amount:"))
        self.Amount = int(self.Amount) + amt
        print("Amount Deposited and balance is :",self.Amount)

    def Withdraw(self):
        amt = int(input("Withdraw amount :"))
        if amt < self.Amount:
            self.Amount = int(self.Amount) - amt
            print("Amount withdrawn and balance is :",self.Amount)


        else:
            print("Not sufficient balance")


    def CalculateInterest(self):
        print("Rate of interest is :", (self.Amount * BankAccount.ROI)/100)

def main():
    baobj = BankAccount("khalid","5000")
    baobj.Display()
    baobj.Deposite()
    baobj.Withdraw()
    baobj.CalculateInterest()


if __name__ == "__main__":
    main()
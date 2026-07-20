#3Write a Python program to implement a class named Numbers with the following specifications:
# The class should contain one instance variable:
# Value
# Define a constructor (_init_) that accepts a number from the user and initializes Value.
# Implement the following instance methods:
# ChkPrime() - returns True if the number is prime, otherwise returns False.
# ChkPerfect() - returns True if the number is perfect, otherwise returns False.
# Factors() - displays all factors of the number.
# SumFactors() - returns the sum of all factors.
# Create multiple objects and call all methods.


class Numbers:


    def _init_(self, number):
        self.Value = number

    def ChkPrime(self):
        count = 0
        for i in range(int(self.Value)):
            num = i+1
            if ((self.Value % num == 0)):
                count = count + 1

            if count == 2:
                return True
            else:
                return False



    def ChkPerfect(self):
        sum = 0
        for i in range(self.Value):
            num = i+1
            if self.Value % num == 0 and self.Value != num:
                sum = sum + num
        if self.Value == sum:
            return True
        else:
            return False


    def Factors(self):
        factorList = []
        for i in range(self.Value):
            num = i+1
            if self.Value % num == 0:
                factorList.append(num)
                print("Factors are :",factorList)



    def SumFactors(self):
        factorList = []
        for i in range(self.Value):
            num = i+1
            if self.Value % num == 0:
                factorList.append(num)
                print("Sum of Factors are :",sum(factorList))


def main():
    number = int(input("Enter a number :"))
    NumObj = Numbers(number)
    isPrime = NumObj.ChkPrime()
    if isPrime:
        print("Number is prime :",isPrime)
    else:
        print("Number is not a prime :",isPrime)


    isPerfect = NumObj.ChkPerfect()
    if isPerfect:
        print("Number is Perfect :",isPerfect)
    else:
        print("Number is not a Perfect :",isPerfect)
    NumObj.Factors()
    NumObj.SumFactors()


if __name__ == "__main__":
    main()
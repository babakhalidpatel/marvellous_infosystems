#write a lambda function using reduce() which accepts list of numbers and returns addition of all elements
from functools import reduce


additionOfNumbers = lambda no1,no2: no1 + no2


def main():
    if __name__ == "__main__":
        array = [1,2,3,4,5,6,7,8,9,10]
        res = reduce(additionOfNumbers, array)
        print("Addition of numbers is :",res)
main()
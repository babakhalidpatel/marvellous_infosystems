# Write a program which contains filter(), map() and reduce() in it. Python application which contains one 
# list of numbers. List contains the numbers which are accepted from user. Filter should filter out all
# such numbers which are even. Map function will calculate its square. reduce will return addition of all that numbers
from functools import reduce


def evenNumber(no):
    return no % 2 == 0

def calculateSquare(no):
    return no * no

def additionOfAll(no1, no2):
    return no1 + no2

def main():
    if __name__ == "__main__":
        no1 = int(input("Enter how many Numbers :"))
        arr = []
        for i in range(1, no1 + 1):
            arr.append(int(input()))
        
        evenList = list(filter(evenNumber, arr))
        sqaureList = list(map(calculateSquare, evenList))
        additionOfAllNumners = reduce(additionOfAll, sqaureList)
        print("Final result is :", additionOfAllNumners)

main()
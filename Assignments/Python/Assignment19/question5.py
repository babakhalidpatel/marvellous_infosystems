# Write a program which contains filter(), map() and reduce() in it. Python application which contains one 
# list of numbers. List contains the numbers which are accepted from user. Filter should filter out all
# all prime numbers. Map function will multiply each number by 2. reduce will return maximum number from that numbers
from functools import reduce

def checkPrime(no):
    count = 0
    for i in range(2, no + 1):
        if no % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False


def multiplyBy2(no):
    return no * 2

def maxOfAllNumbers(no1, no2):
    return max(no1, no2)

def main():
    if __name__ == "__main__":
        no1 = int(input("Enter how many Numbers :"))
        arr = []
        for i in range(1, no1 + 1):
            arr.append(int(input()))
        
        primeList = list(filter(checkPrime, arr))
        multiplyBy2List = list(map(multiplyBy2, primeList))
        additionOfAllNumners = reduce(maxOfAllNumbers, multiplyBy2List)
        print("Final result is :", additionOfAllNumners)

main()
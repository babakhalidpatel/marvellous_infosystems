# Write a program which contains filter(), map() and reduce() in it. Python application which contains one 
# list of numbers. List contains the numbers which are accepted from user. Filter should filter out all
# such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10.
# Reduce will return product of all that numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000

from functools import reduce


def GreaterOrThan70OrLessThan90(no):
    return no >= 70 and no <= 90

def IncreaseBy10(no):
    return no + 10

def ProdcutOfAllNumbers(no1, no2):
    return no1 * no2

def main():
    if __name__ == "__main__":
        no1 = int(input("Enter how many Numbers :"))
        arr = []
        for i in range(1, no1 + 1):
            arr.append(int(input()))
        
        Greterthan70andLessThan90List = list(filter(GreaterOrThan70OrLessThan90, arr))
        IncreaseBy10List = list(map(IncreaseBy10, Greterthan70andLessThan90List))
        productOfFinalNumbers = reduce(ProdcutOfAllNumbers, IncreaseBy10List)
        print("Final Product result is :", productOfFinalNumbers)

main()
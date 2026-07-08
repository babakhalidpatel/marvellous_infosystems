# write a program which accept N numbers from user and store it into List. return addition of all prime numbers from that list
# Main python file accept N numbers from user and pass each number to ChkPrime() function which is part of our user defined 
# module named as marvellousNum. name of the function from main python file should be listPrime()

from marvellousNum import ChkPrime


def listPrime(arr):
    primeList = []
    for i in arr:
        if(ChkPrime(i) == True):
            primeList.append(i)
    return primeList

def AdditionOfPrimeNumners(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum

def main():
    no = int(input("Number of Elements :"))
    arr = []
    for i in range(no):
        if i == 0:
            arr.append(int(input(f"Enter {i+1}st element :")))
        elif i == 1:
            arr.append(int(input(f"Enter {i+1}nd element :")))
        elif i == 2:
            arr.append(int(input(f"Enter {i+1}rd element :")))
        else:
            arr.append(int(input(f"Enter {i+1}th element :")))

    primeNumberList = listPrime(arr)
    addition = AdditionOfPrimeNumners(primeNumberList)
    additionList = ""
    for i in primeNumberList:
        if additionList == "":
            additionList = str(i)
        else:
            additionList = additionList + f" + {str(i)}"

    print(str(addition) + " (" + additionList + ")")


main()
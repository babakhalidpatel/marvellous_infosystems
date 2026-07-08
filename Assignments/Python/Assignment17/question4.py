#write a program which accept one number from user and return addition of its factors

def additionOfFactors(no):
    sum = 0
    arr = []
    for i in range(1, no):
        if no % i == 0:
            arr.append(i)
    for i in arr:
        sum = sum + i
    return sum

def main():
    if __name__ == "__main__":
        no = int(input("Enter a number :"))
        factAdd = additionOfFactors(no)
        print("Addition of factors is :", factAdd)

main()
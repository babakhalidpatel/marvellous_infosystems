#write a program which accept one number from user and whether number is prime or not

def checkPrime(no):
    count = 0
    for i in range(2, no + 1):
        if no % i == 0:
            count = count + 1
    if count == 1 :
        return True
    else:
        return False


def main():
    if __name__ == "__main__":
        no = int(input("Enter a number :"))
        prime = checkPrime(no)
        if prime == True:
            print("It is prime numner")
        else:
            print("It is not a prime number")

main()
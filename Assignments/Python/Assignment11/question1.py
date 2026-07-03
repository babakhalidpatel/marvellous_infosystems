#write a program which accepts one number and checks whether it is prime or not

def PrimeNumber(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        print("Given Number",num,"is a Prime")
    else:
        print("Given Number",num,"is non Prime")


def main():
    if __name__ == "__main__":
        PrimeNumber(int(input("Enter a number: ")))
main()
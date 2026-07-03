#write a program which accept one number and prints factorial of that number

def Factorial(num):
    fact = 1

    for i in range(1, num+1):
        fact = fact * i
    print("Factorial is :",fact)
    


def main():
    if __name__ == "__main__":
        Factorial(int(input("Enter a number: ")))

main()
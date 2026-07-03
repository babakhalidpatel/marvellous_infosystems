#write a program which accepts one number and prints its factors

def FactorNumber(no):

    for i in range(1, no+1):
        if no%i == 0:
            print(i)

def main():
    if __name__ == "__main__":
        FactorNumber(int(input("Enter a number :")))

main()
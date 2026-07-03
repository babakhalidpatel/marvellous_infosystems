#write a program which accept one number and checks whether it is divisible by 3 and 5

def IsDivisibleBy3or5(no):
    if no%3 == 0 or no%5 == 0:
        print("Number is divisible by 3 or 5")
    else:
        print("Sorry, it is not")

def main():
    if __name__ == "__main__":
        no = int(input("Enter a number :"))
        IsDivisibleBy3or5(no)

main()

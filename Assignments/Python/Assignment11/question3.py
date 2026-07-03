#write a program which accepts one number and print sum of digits
def SumOfNumbers(no):
    sum = 0

    while no > 0:
        sum = sum + (no%10)
        no = int(no / 10)
    
    print("Sum is : ", sum)

def main():
    if __name__ == "__main__":
        SumOfNumbers(int(input("Enter a number :")))
    
main()
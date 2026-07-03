#write a program which accepts one number and prints sum of first N natural numbers.
def SumOfFirstNNumber(no):
    start = 0
    sum = 0
    while no != start:
        sum = sum + no
        no = no - 1
    print("Sum of all numbers till given number is :", sum)

def main():
    if __name__ == "__main__":
        SumOfFirstNNumber(int(input("Enter a number: ")))
main()
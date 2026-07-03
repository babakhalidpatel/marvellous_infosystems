# write a program which accepts one number and prints binary equivalent

def BinaryOfNumber(num):
    binary = ''
    while num > 0:
        binary = str(num % 2) + binary
        num = int(num / 2)
    print("Binary equivalent is :", binary)


def main():
    if __name__ == "__main__":
        BinaryOfNumber(int(input("Enter a number :")))

main()
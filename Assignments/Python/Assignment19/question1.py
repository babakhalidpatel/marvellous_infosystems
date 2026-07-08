# write a program which contains one lambda function which accepts one parameter and return power of two

powerOfTwo = lambda no : no * no

def main():
    if __name__ == "__main__":
        no = int(input("Enter a Number :"))
        print("2's power of this number is :", powerOfTwo(no))

main()
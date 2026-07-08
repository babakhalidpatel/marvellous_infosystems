# write a program which contains one lambda function which accepts two parameters and returns its multiplication
multOfTwo = lambda no1, no2 : no1 * no2

def main():
    if __name__ == "__main__":
        no1 = int(input("Enter first Number :"))
        no2 = int(input("Enter Second Number :"))
        print("Multplication of numbers is :", multOfTwo(no1, no2))

main()
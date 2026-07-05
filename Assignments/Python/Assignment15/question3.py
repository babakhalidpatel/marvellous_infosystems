#write a lambda function using filter() which accepts list of numbers and returns a list of odd number.

oddNumbers = lambda no: no % 2 != 0


def main():
    if __name__ == "__main__":
        array = [1,2,3,4,5,6,7,8,9,10]
        res = list(filter(oddNumbers, array))
        print("List of odd numbers is :",res)
main()
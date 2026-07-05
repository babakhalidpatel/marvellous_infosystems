#write a lambda function using filter() which accepts list of numbers and resturns a list of even number.

evenNumber = lambda no: no % 2 == 0


def main():
    if __name__ == "__main__":
        array = [1,2,3,4,5,6,7,8,9,10]
        res = list(filter(evenNumber, array))
        print("List of even numbers is :",res)
main()
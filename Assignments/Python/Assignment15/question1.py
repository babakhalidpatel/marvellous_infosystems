#write a lambda function using map() which accepts list of numbers and resturns a list of square of each number.

squareOfEachNumber = lambda no: no * no 


def main():
    if __name__ == "__main__":
        array = [1,2,3,4,5]
        res = list(map(squareOfEachNumber, array))
        print("List of squares is :",res)
main()
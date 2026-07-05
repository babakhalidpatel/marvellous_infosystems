#write a lambda function using reduce() which accepts list of numbers and returns minimum element


from functools import reduce


maxNumbers = lambda no: min(no)


def main():
    if __name__ == "__main__":
        array = [1,2,3,4,5,6,7,8,9,10]
        res = maxNumbers(array)
        print("Maximum number is :",res)
main()
#write a lambda function using filter() which accepts a list of numbers and return list of numbers divisible by 3 and 5

divisibleBy3and5 = lambda no: no % 3 == 0 or no % 5 == 0


def main():
    if __name__ == "__main__":
        array = [1,2,3,4,5,6,7,8,9,10]
        res = list(filter(divisibleBy3and5, array))
        print("Divisible by 3 and 5 numbers are:",res)
main()
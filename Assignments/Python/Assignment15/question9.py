#write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements

from functools import reduce


productOfAllElement = lambda no1, no2: no1 * no2


def main():
    if __name__ == "__main__":
        array = [1,2,3,4,5]
        res = reduce(productOfAllElement, array)
        print("Product of all elements is:",res)
main()
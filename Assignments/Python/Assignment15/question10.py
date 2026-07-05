#write a lambda function using filter() which accepts a list of numbers the count of even numbers in the list

countOfEvenNumbers = lambda no: no % 2 == 0

def main():
    if __name__ == "__main__":
        array = [1,2,3,4,5,6,7,8,9,10]
        res = list(filter(countOfEvenNumbers, array))
        print("Count of even numbers in the list is:",len(res))
main()
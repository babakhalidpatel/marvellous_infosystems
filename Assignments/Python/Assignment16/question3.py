#write a program which contains one function named as Add(). which accept two numbers from user and return addition of that number
def Add(no1, no2):
    return no1 + no2

def main():
    if __name__ == "__main__":
        no1 = int(input("Enter a first number :"))
        no2 = int(input("Enter a Second number :"))
        ret = Add(no1, no2)
        print("Addition is :", ret)

main()
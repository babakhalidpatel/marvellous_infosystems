#write a lambda function which accepts three numbers and returns largest number
MaxNumber =  lambda no1,no2,no3 : {'first':((no1 > no2) and (no1 > no3)) , 'second':((no2 > no1) and (no2 > no3)) }

def main():
    if __name__ == "__main__":
        res = MaxNumber(int(input("Enter first number :")),int(input("Enter second number :")), int(input("Enter third number :")))
        if res['first'] == True:
            print("First entered number is largest")
        elif res['second'] == True:
            print("Second entered number is largest")
        else:
            print("Third entered number is largest")
       
main()
#write a program which accept one number and print reverse of that number

def Reverse(no):
    reverse = ''
    while no > 0:
        reverse = reverse + str(no%10)
        no = int(no / 10)
    
    print("Reverse number is :",reverse)

def main():
    if __name__ == "__main__":
        Reverse(int(input("Enter a number :")))

main()
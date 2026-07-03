#write a program which accept one number and check whether its palindrome or not

def Palindrome(no):
    reverse = ''
    original = no
    while no > 0:
        reverse = reverse + str(no%10)
        no = int(no / 10)

    if reverse == str(original):
        print("It is palindrome")
    else:
        print("It is not palindrome")
    

def main():
    if __name__ == "__main__":
        Palindrome(int(input("Enter a number :")))

main()
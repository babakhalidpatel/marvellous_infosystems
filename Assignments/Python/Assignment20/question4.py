

import threading

def Small(data):
    count = 0
    for char in data:
        if str.islower(char):
            count += 1
    print("This many are small letters :",count)

def Capital(data):
    count = 0
    for char in data:
        if str.isupper(char):
            count += 1
    print("This many are capital letters :",count)
    
def Digits(data):
    count = 0
    for char in data:
        if str.isdigit(char):
            count += 1
    print("This many are digits :",count)
    
def main():
    if __name__ == "__main__":
        string = str(input("Enter a string : "))
        t1 = threading.Thread(target=Small, args=[string, ])
        t2 = threading.Thread(target=Capital, args=[string, ])
        t3 = threading.Thread(target=Digits, args=[string, ])
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()
        print("Exit from main")
main()
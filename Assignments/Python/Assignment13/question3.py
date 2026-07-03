# write a program which accepts one number and checks whether it is perfect number or not

def IsPerfect(no):
    sum = 0
    original = no
    for i in range(1, no):
        if no % i == 0:
            sum = sum + i
    if sum == original:
        print("It is perfect number")
    else:
        print("It is not perfect number")



def main():
    if __name__ == "__main__":
        IsPerfect(int(input("Enter a number :")))

main()
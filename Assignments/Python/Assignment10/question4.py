#write a program which accepts one number and prints all even numbers till that number

def PrintEvenNumbersTillNNumbers(num):
    
    for i in range(1, num+1):
        if i%2 == 0:
            print(i)
def main():
    if __name__ == "__main__":
        PrintEvenNumbersTillNNumbers(int(input("Enter a number :")))

main()
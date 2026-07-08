#write a program which accept one number and display below pattern
# * * * * *
# * * * *
# * * *
# * *
# *

def starPattern(no):
    
    for i in range(no, 0, -1):
        print("* "*i)


def main():
    if __name__ == "__main__":
        no = int(input("Enter a number :"))
        starPattern(no)
main()
#write a program which accept one number and display below pattern
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

def numberPattern(no):
    pattern = ""
    for i in range(1, no + 1):
        pattern += str(i) + " "

    for j in range(1, no + 1):
        print(pattern)


def main():
    if __name__ == "__main__":
        no = int(input("Enter a number :"))
        numberPattern(no)
main()
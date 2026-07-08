#write a program which accept one number and display below pattern
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

def numberPattern(no):
    pattern = ""
    for i in range(1, no + 2):
        if pattern == "":
            pattern += str(i) + " "
        else:
            print(pattern)
            pattern += str(i) + " "


def main():
    if __name__ == "__main__":
        no = int(input("Enter a number :"))
        numberPattern(no)
main()
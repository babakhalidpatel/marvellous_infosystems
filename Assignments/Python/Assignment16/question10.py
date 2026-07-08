#write a program which accept name from user and display length of its name.

def lengthOfString(data):
    return len(data)

    
def main():
    if __name__ == "__main__":
        ret = lengthOfString(str(input("Enter a string :")))
        print(ret)

main()
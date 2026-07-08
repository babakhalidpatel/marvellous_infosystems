#write a program which display 10 to 1 on screen

def Display10To1():
    res = ""
    for i in range(10, 0, -1):
        res = str(res) + " " + str(i)
    print(res)

def main():
    if __name__ == "__main__":
        Display10To1()

main()
#write a program which accept n numbers from user and store it into list. return addition of all element from that list

def AdditionOfAllElements(ele):
    sum = 0
    for i in ele:
        sum = sum + i
    return sum

def main():
    no = int(input("Number of elements :"))
    arr = []
    for i in range (no):
        arr.append(int(input()))
    res = AdditionOfAllElements(arr)
    print(res)

main()

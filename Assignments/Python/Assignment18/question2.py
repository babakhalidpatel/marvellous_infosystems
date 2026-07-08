#write a program which accept n numbers from user and store it into list. return maximum number from that list

def maxNumberFromList(ele):
    return max(ele)

def main():
    no = int(input("Number of elements :"))
    arr = []
    for i in range (no):
        arr.append(int(input()))
    res = maxNumberFromList(arr)
    print(res)

main()

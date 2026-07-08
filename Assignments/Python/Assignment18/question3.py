#write a program which accept n numbers from user and store it into list. return minimum number from that list

def minNumberFromList(ele):
    return min(ele)

def main():
    no = int(input("Number of elements :"))
    arr = []
    for i in range (no):
        arr.append(int(input()))
    res = minNumberFromList(arr)
    print(res)

main()

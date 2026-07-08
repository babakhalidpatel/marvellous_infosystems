#write a program which accept n numbers from user and store it into list. 
#accept one number from user and return frequency of that number


def elementsToSearch(ele, search):
    count = 0
    for i in ele:
        if i == search:
            count = count + 1
    return count

def main():
    no = int(input("Number of elements :"))
    arr = []
    print("Enter elements 1 by 1 and keep entring enter - ")
    for i in range (no):
        arr.append(int(input()))
    search = int(input("Elements to search :"))
    res = elementsToSearch(arr, search)
    print(res)
main()

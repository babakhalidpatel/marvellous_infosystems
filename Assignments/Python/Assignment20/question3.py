

import threading

def EvenList(arr):
    sum = 0
    for i in arr:
        if i % 2 == 0:
            sum = sum + i
    print("Even Factor sum is", sum)

def OddList(arr):
    sum = 0
    for i in arr:
        if i % 2 != 0:
            sum = sum + i
    print("Odd Factor sum is", sum)
    


def main():
    if __name__ == "__main__":
        no = int(input("How many numbers : "))
        arr = []
        for i in range(1, no + 1):
            arr.append(int(input()))
        t1 = threading.Thread(target=EvenList, args=[arr])
        t2 = threading.Thread(target=OddList, args=[arr])
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print("Exit from main")
main()


import threading

def evenFactor(no):
    sum = 0
    for i in range(1, no+1):
        if i % 2 == 0:
            sum = sum + i
    print("Even Factor sum is", sum)

def oddFactor(no):
    sum = 0
    for i in range(1, no+1):
        if i % 2 != 0:
            sum = sum + i
    print("Odd Factor sum is", sum)
    


def main():
    if __name__ == "__main__":
        no = int(input("Enter a number : "))
        t1 = threading.Thread(target=evenFactor, args=[no,])
        t2 = threading.Thread(target=oddFactor, args=[no,])
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print("Exit from main")
main()


import threading

def print1to50():
    for i in range(1, 51):
        print(i)

def print50to1():
    for i in range(50, 0, -1):
        print(i)

    
def main():
    if __name__ == "__main__":
        print("first thread started")
        t1 = threading.Thread(target=print1to50)
        t2 = threading.Thread(target=print50to1)
        t1.start()
        t1.join()
        print("Second thread started")
        t2.start()
        t2.join()
        print("Exit from main")
main()
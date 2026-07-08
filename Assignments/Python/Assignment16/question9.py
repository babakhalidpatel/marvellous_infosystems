#write a program which display first 10 even numbers in screen

def displayFirst10EvenNumbers():
    arr = []
    for i in range(2, 100, 2):
        arr.append(i)
        if len(arr) > 9:
            break
    print(arr)

    
def main():
    if __name__ == "__main__":
        displayFirst10EvenNumbers()

main()
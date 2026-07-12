#2: Design a Python application that creates two threads.

#Thread 1 should calculate and display the maximum element from a list.
#Thread 2 should calculate and display the minimum element from the same list.
#The list should be accepted from the user.

def find_max(numbers):
    max_num = max(numbers)
    print("Maximum number:", max_num)

def find_min(numbers):
    min_num = min(numbers)
    print("Minimum number:", min_num)

def main():
    import threading

    # Accepting a list of integers from the user
    user_input = input("Enter a list of integers separated by spaces: ")
    numbers = list(map(int, user_input.split()))

    max_thread = threading.Thread(target=find_max, args=(numbers,))
    min_thread = threading.Thread(target=find_min, args=(numbers,))

    max_thread.start()
    min_thread.start()

    max_thread.join()
    min_thread.join()

if __name__ == "__main__":
    main()
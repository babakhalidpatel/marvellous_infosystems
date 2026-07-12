#10: Design a Python application that creates two threads.

#Thread 1 should compute the sum of elements from a list.
#Thread 2 should compute the product of elements from the same list.
#Return the results to the main thread and display them.

def compute_sum(numbers, result):
    result[0] = sum(numbers)

def compute_product(numbers, result):
    product = 1
    for num in numbers:
        product *= num
    result[0] = product

def main():
    import threading

    # Accepting a list of integers from the user
    user_input = input("Enter a list of integers separated by spaces: ")
    numbers = list(map(int, user_input.split()))

    sum_result = [0]
    product_result = [0]

    sum_thread = threading.Thread(target=compute_sum, args=(numbers, sum_result))
    product_thread = threading.Thread(target=compute_product, args=(numbers, product_result))

    sum_thread.start()
    product_thread.start()

    sum_thread.join()
    product_thread.join()

    print("Sum of elements:", sum_result[0])
    print("Product of elements:", product_result[0])

if __name__ == "__main__":
    main()
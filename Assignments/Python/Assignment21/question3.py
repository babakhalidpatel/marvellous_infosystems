#3: Design a Python application where multiple threads update a shared variable.

#Use a Lock to avoid race conditions.
#Each thread should increment the shared counter multiple times.
#Display the final value of the counter after all threads complete execution.

def increment_counter(counter, lock, increments):
    for _ in range(increments):
        with lock:
            counter[0] += 1

def main():
    import threading

    # Shared counter variable
    counter = [0]
    lock = threading.Lock()
    increments_per_thread = 1000
    num_threads = 5

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=increment_counter, args=(counter, lock, increments_per_thread))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Final value of the counter:", counter[0])

if __name__ == "__main__":
    main()
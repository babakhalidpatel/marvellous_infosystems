# 1: Design a Python application that creates two threads named Prime and NonPrime.

#Both threads should accept a list of integers.
#The Prime thread should display all prime numbers from the list.
#The NonPrime thread should display all non-prime numbers from the list.

def prime_numbers(numbers):
    primes = []
    for num in numbers:
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    print("Prime numbers:", primes)

def non_prime_numbers(numbers):
    non_primes = []
    for num in numbers:
        if num <= 1:
            non_primes.append(num)
        else:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    is_prime = False
                    break
            if not is_prime:
                non_primes.append(num)
    print("Non-prime numbers:", non_primes)

def main():
        import threading

        numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        prime_thread = threading.Thread(target=prime_numbers, args=(numbers,))
        non_prime_thread = threading.Thread(target=non_prime_numbers, args=(numbers,))

        prime_thread.start()
        non_prime_thread.start()

        prime_thread.join()
        non_prime_thread.join()

if __name__ == "__main__":
    main()

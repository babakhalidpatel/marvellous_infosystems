#For every number in the given list, count how many prime numbers exist between 1 and N using multiprocessing Pool.

#Example
#10000
#20000
#30000
#40000
#Display

#Total prime count for each number.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(n):
    return sum(1 for i in range(2, n + 1) if is_prime(i))

if __name__ == "__main__":
    from multiprocessing import Pool

    numbers = [10000, 20000, 30000, 40000]
    
    with Pool() as pool:
        results = pool.map(count_primes, numbers)
    
    for num, prime_count in zip(numbers, results):
        print(f"Total prime count for {num}: {prime_count}")
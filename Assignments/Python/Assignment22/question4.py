#Write a program that calculates

#1^5 + 2^5 + 3^5 + ..... + N^5

#for multiple values of N simultaneously using Pool.

#Input
#[1000000,
#2000000,
#3000000,
#4000000]
#Display

#Measure total execution time.

def sum_of_fifth_powers(n):
    return sum(i**5 for i in range(1, n + 1))

if __name__ == "__main__":
    from multiprocessing import Pool
    import time

    numbers = [1000000, 2000000, 3000000, 4000000]
    
    start_time = time.time()
    
    with Pool() as pool:
        results = pool.map(sum_of_fifth_powers, numbers)
    
    end_time = time.time()
    
    for num, result in zip(numbers, results):
        print(f"Sum of fifth powers up to {num}: {result}")
    
    print(f"Total execution time: {end_time - start_time} seconds")
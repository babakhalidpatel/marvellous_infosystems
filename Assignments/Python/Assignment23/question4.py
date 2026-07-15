#Write a program that counts how many odd numbers exist between 1 and n.

#Input
#Data = [1000000, 2000000, 3000000, 4000000]
#Expected Output Format
#Process ID : 1237
#Input Number : 1000000
#Odd Number Count : 500000

def count_odd_numbers(n):
    return (n + 1) // 2

if __name__ == "__main__":
    from multiprocessing import Pool
    import os

    numbers = [1000000, 2000000, 3000000, 4000000]
    
    with Pool() as pool:
        results = pool.map(count_odd_numbers, numbers)
    
    for num, odd_count in zip(numbers, results):
        print(f"Process ID: {os.getpid()}, Input Number: {num}, Odd Number Count: {odd_count}")
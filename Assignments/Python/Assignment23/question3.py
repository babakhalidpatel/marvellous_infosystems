#Write a program that counts how many even numbers exist between 1 and n using Pool.map().

#Input
#Data = [1000000, 2000000, 3000000, 4000000]
#Expected Output Format
#Process ID : 1236
#Input Number : 1000000
#Even Number Count : 500000

def  count_even_numbers(n):
    return n // 2

if __name__ == "__main__":
    from multiprocessing import Pool
    import os

    numbers = [1000000, 2000000, 3000000, 4000000]
    
    with Pool() as pool:
        results = pool.map(count_even_numbers, numbers)
    
    for num, even_count in zip(numbers, results):
        print(f"Process ID: {os.getpid()}, Input Number: {num}, Even Number Count: {even_count}")
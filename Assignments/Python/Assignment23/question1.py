#Write a Python program using multiprocessing.Pool to calculate the sum of all even numbers from 1 to N for every number from the given list.

#Input
#Data = [1000000, 2000000, 3000000, 4000000]
#Expected Task

#For each number N, calculate:

#2 + 4 + 6 + ... + N
#Expected Output Format
#Process ID : 1234
#Input Number : 1000000
#Sum of Even Numbers : 250000500000

def sum_of_even_numbers(n):
    return sum(i for i in range(2, n + 1, 2))

if __name__ == "__main__":
    from multiprocessing import Pool
    import os

    numbers = [1000000, 2000000, 3000000, 4000000]
    
    with Pool() as pool:
        results = pool.map(sum_of_even_numbers, numbers)
    
    for num, even_sum in zip(numbers, results):
        print(f"Process ID: {os.getpid()}, Input Number: {num}, Sum of Even Numbers: {even_sum}")
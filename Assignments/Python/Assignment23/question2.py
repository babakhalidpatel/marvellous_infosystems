#Write a Python program using multiprocessing.Pool to calculate the sum of all odd numbers from 1 to n.

#Input
#Data = [1000000, 2000000, 3000000, 4000000]
#Expected Task

#For each number N, calculate:

#1 + 3 + 5 + ... + N
#Expected Output Format
#Process ID : 1235
#Input Number : 1000000
#Sum of Odd Numbers : 250000000000

def sum_of_odd_numbers(n):
    return sum(i for i in range(1, n + 1, 2))

if __name__ == "__main__":
    from multiprocessing import Pool
    import os

    numbers = [1000000, 2000000, 3000000, 4000000]
    
    with Pool() as pool:
        results = pool.map(sum_of_odd_numbers, numbers)
    
    for num, odd_sum in zip(numbers, results):
        print(f"Process ID: {os.getpid()}, Input Number: {num}, Sum of Odd Numbers: {odd_sum}")
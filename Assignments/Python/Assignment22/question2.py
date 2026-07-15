#write a program that calculates factorials of multiple numbers simultaneously using Pool.map().

#Input
#[10, 15, 20, 25]
#Display
#Process ID
#Input Number
#Factorial

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
if __name__ == "__main__":
    from multiprocessing import Pool
    import os

    numbers = [10, 15, 20, 25]
    
    with Pool() as pool:
        results = pool.map(factorial, numbers)
    
    for num, fact in zip(numbers, results):
        print(f"Process ID: {os.getpid()}, Input Number: {num}, Factorial: {fact}")
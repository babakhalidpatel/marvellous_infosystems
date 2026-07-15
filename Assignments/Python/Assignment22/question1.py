#Write a program that accepts a list of integers and uses Pool.map() to calculate the sum of squares from 1 to N for every element in the list.
#input: [1000000,2000000,3000000,4000000]
#output [
#333333833333500000,
#2666668666667000000,
#...
#]

from multiprocessing import Pool

def sum_of_squares(n):
    return sum(i**2 for i in range(1, n + 1))

if __name__ == "__main__":
    numbers = [1000000, 2000000, 3000000, 4000000]
    with Pool() as pool:
        results = pool.map(sum_of_squares, numbers)
    print(results)
# module

def ChkPrime(no):
    divisibleCount = 0
    for i in range(2, no+1):
        if no % i == 0:
            divisibleCount = divisibleCount + 1
    if divisibleCount == 1:
        return True
    else:
        return False
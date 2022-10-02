"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if(number_of_primes<1):
        raise ValueError("No numbers less than 1")
        return
    list = []
    count = 0
    number = 2
    while count < number_of_primes:
        for n in range(2,number):
            if(number % n == 0):
                break
        else:
            count+=1
            list.append(number)
        number+=1
    return list

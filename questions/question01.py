"""
Find the all prime numbers up to 1M
"""
import math
import time

t = time.process_time()

primes = [2]
for prime in range(3, 1000000, 2):
    is_prime = True
    divisor = 3
    sqrt_of_prime = math.sqrt(prime)
    while divisor <= sqrt_of_prime and is_prime:
        if prime % divisor == 0:
            is_prime = False
        divisor += 1
    if is_prime:
        primes.append(prime)
elapsed_time = time.process_time() - t
print("Duration: {}".format(elapsed_time))
print(primes)
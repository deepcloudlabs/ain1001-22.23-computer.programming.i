"""
Store Fibonacci sequence of leading 100 elements in a list
"""
fibonacci = [0, 1]
while len(fibonacci) < 100:
    n = len(fibonacci)
    fibonacci.append(fibonacci[n - 1] + fibonacci[n - 2])
print(fibonacci)

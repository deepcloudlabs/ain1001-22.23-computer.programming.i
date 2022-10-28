"""
How can you swap two variables without using variable?
"""
x = 53
y = 47
print(f"Initially, x holds {x} and y holds {y}")
x = x ^ y
y = x ^ y
x = x ^ y
print(f"Some magic...then, x holds {x} and y holds {y}")

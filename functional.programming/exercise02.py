import builtins
from functools import reduce

from utility.math import is_even, to_cube

numbers = [4, 8, 23, 16, 15, 42]


#         [4,    8,   16,    42] after filter
#         [64, 512, 4096, 74088] after map
#         s=0, (0,64) -> s=64, (64,512) -> 576, (576,4096)-> 4672
#         (4672,74088) -> 78760
def topla(x, y):
    print(f"topla --> x: {x}, y: {y}")
    return x+y


solution = reduce(topla, map(lambda n: n ** 3, filter(lambda u: u % 2 == 0, numbers)), 0)
print(solution)

solution = reduce(lambda s,u: s+u, map(lambda n: n ** 3, filter(lambda u: u % 2 == 0, numbers)), 0)
print(solution)

solution = sum(map(lambda n: n ** 3, filter(lambda u: u % 2 == 0, numbers)), 0)
print(solution)

from math import sqrt


def get_triangle_area(a, b, c):
    #  if a>0 and b>0 and c>0:
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All side lengths must be positive!")
    if (a + b) > c or (a + c) > b or (b + c) > a:
#   if ((a + b) <= c) and ((a + c) <= b) and (b + c) <= a:
        s = 0.5 * (a + b + c)
        return sqrt(s * (s - a) * (s - b) * (s - c))
    raise ValueError("This is not a valid triangle!")


print(f"get_triangle_area(4,13,15): {get_triangle_area(8, 4, 5)}")

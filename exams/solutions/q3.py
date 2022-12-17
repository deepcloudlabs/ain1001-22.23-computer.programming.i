# median
def fun(t):
    a, b, c = t
    if a <= b <= c:
        return b
    elif b <= a <= c:
        return a
    else:
        return c


for u in [(7, 2, 4), (22, 15, 33), (14, 15, 16)]:
    print(f"fun({u}): {fun(u)}")

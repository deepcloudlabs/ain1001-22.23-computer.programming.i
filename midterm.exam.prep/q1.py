def fun(x):
    # y = a x + b
    if x <= -5:  # region #1
        a = 0
        b = 0
    elif x > 1:  # region #4
        a = 0
        b = 1
    elif -5 < x <= -2:  # region #2
        a = 4.0 / 3.0
        b = 20.0 / 3.0
    elif -2 < x <= 1:  # region #3
        a = -1
        b = 2
    return a * x + b


x_values = [-10, -5, -4, -3, -2, -1.5, -1, 0, 0.5, 1, 2]
for x in x_values:
    print(f"fun({x}): {fun(x)}")

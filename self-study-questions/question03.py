"""
A circle in a two-dimensional Cartesian coordinate system could be represented by
three parameters: radius r and center coordinates (x,y).

Write a main function which reads these three parameters for the two circles, A and B, and
decides on one of the following cases:
1) One circle contains the other one
2) Intersection
3) Disjoint (This is the case given in the figure)

The output of the program is the case number explained above.
"""
xa = float(input("Enter x: "))
ya = float(input("Enter y: "))
ra = float(input("Enter r: "))
xb = float(input("Enter x: "))
yb = float(input("Enter y: "))
rb = float(input("Enter r: "))
r = (xb - xa) ** 2 + (yb - ya) ** 2
r_min = ra
r_max = rb
if rb < ra:
    r_min = rb
    r_max = ra
elif xa == xb and ya == yb and ra == rb:
    print("Case II - Intersection (identical circles)")
elif ((r_min + r) * (r_min + r)) < (r_max * r_max):
    print("Case I: One circle contains the other one")
elif ((ra + rb) * (ra + rb)) > r:
    print("Case II: Intersection")
else:
    print("Case III: Disjoint")
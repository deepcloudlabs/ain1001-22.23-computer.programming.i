def get_discriminant(a, b, c):
    return b * b - 4 * a * c


def get_determinant(a, b, c, d):
    return a * d - b * c


def get_characteristic(A, B, C, D, E, F):
    return A * get_determinant(C, E / 2, E / 2, F)
    - (B / 2) * get_determinant(B / 2, E / 2, D / 2, F)
    + (D / 2) * get_determinant(B / 2, C, D / 2, E / 2)


def get_type_of_conic(A, B, C, D, E, F):
    discriminant = get_discriminant(A, B, C)
    characteristic = get_characteristic(A, B, C, D, E, F)
    if discriminant == 0 and characteristic != 0:
        return "Nondegenerate Parabola"
    elif discriminant == 0 and characteristic == 0:
        return "Degenerate Parabola"
    elif discriminant < 0 and characteristic != 0:
        return "Nondegenerate ellipse or circle"
    elif discriminant < 0 and characteristic == 0:
        return "Degenerate Ellipse"
    elif discriminant > 0 and characteristic != 0:
        return "Nondegenerate Hyperbola"
    elif discriminant > 0 and characteristic == 0:
        return "Degenerate Hyperbola"

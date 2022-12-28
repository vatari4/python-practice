def roots_of_quadratic_equation(a, b, c):
    D = b ** 2 - 4 * a * c  # дискриминант
    x1 = (-b + D ** 0.5) / (2 * a)  # первый корень
    x2 = (-b - D ** 0.5) / (2 * a)  # второй корень

    if x1 == x2:
        return x1
    else:
        return x1, x2


def solve(*coeffs):
    if len(coeffs) == 3:
        return roots_of_quadratic_equation(*coeffs)
    elif len(coeffs) == 2:
        b, c = coeffs[0], coeffs[1]
        return -c / b
    else:
        return 0


print(sorted(solve(1, 2, 1)))
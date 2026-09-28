def discriminant(a, b, c):
    d = b ** 2 - 4 * a *c
    return d


def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    if a == 0 and b == 0 and c == 0:
        return 'любое число'
    d = discriminant (a, b, c)
    if d < 0:
        result = 'корней нет'
    elif d == 0:
        result = -b / (2 * a)
    else:
        result = ((-b + d ** 0.5)/(2 * a), (-b - d ** 0.5)/(2 * a))
    return result
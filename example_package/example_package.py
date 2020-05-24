"""Main module."""


def prime(n):
    if not n % 2:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True

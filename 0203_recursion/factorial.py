def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


assert factorial(2) == 2
assert factorial(3) == 6
assert factorial(4) == 24

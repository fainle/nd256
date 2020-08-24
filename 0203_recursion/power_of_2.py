def power_of_2(n):
    if n == 0:
        return 1

    return 2 * power_of_2(n - 1)


assert power_of_2(2) == 4
assert power_of_2(3) == 8
assert power_of_2(4) == 16

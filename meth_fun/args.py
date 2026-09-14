def sum_numbers(*args):
    res = 0
    for i in args:
        res += i
    return res

print(sum_numbers())
def sum_numbers(*args):
    res = 0
    for i in args:
        res += i
    return res

numbers = list(map(int, input().split()))
print(sum_numbers(*numbers))
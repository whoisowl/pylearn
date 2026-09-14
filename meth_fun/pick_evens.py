def pick_evens(*args):
    res = []
    for i in args:
        if i % 2 == 0:
            res.append(i)
    return res

numbers = list(map(int, input().split()))
print(pick_evens(*numbers))
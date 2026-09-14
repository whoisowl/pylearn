def skyline(*args):
    if not args:
        return 0
    biggest = args[0]
    for i in args:
        if i > biggest:
            biggest = i
    return biggest

numbers = list(map(int, input().split()))
print(skyline(*numbers))
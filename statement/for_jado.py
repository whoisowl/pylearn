n = int(input())
x = int(input())

for i in range(n):
    if x % 2 == 0:
        x = (x / 2)
    elif x % 2 == 1:
        x = (x * 2) - 1
    
print(int(x))
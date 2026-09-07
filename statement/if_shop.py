qeimat = int(input())

if qeimat > 50000:
    final_price = qeimat * 0.8
elif qeimat >= 20000:
    final_price = qeimat * 0.9
else:
    final_price = qeimat

print(int(final_price))
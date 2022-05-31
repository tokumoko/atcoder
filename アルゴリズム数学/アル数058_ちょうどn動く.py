n, x, y = map(int, input().split())
if n % 2 == (x+y) % 2 and n >= (abs(x) + abs(y)):
    print('Yes')
else:
    print('No')
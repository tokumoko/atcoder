a, b, c = map(int, input().split())
if b < c:
    b, c = c, b
if a < b:
    a, b = b, a
if b < c:
    b, c = c, b
if a - b <= c:
    print(a)
else:
    print(-1)
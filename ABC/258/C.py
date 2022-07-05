n, q = map(int, input().split())
s = input()
up = 0
for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        up += x
    else:
        print(s[(x-1 - up) % n])

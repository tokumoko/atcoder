n, q = map(int, input().split())
a = list(map(int, input().split()))
slide = 0
for i in range(q):
    t, x, y = map(int, input().split())
    x -= slide + 1
    y -= slide + 1
    #if x < 0:x += n
    #if y < 0:y += n
    if t == 1:
        a[x], a[y] = a[y], a[x]
    elif t == 2:
        slide += 1
    else:
        print(a[x])
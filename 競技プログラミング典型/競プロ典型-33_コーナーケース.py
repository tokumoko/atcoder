h, w = map(int, input().split())
if h != 1 and w != 1:
    print(((h+1) // 2) * ((w+1) // 2))
else:
    print(h * w)
h1, h2, h3, w1, w2, w3 = map(int, input().split())
ans = 0
for a in range(1, h1-1):
    for b in range(1, h1-a):
        for c in range(1, w1-a):
            for d in range(1, min(h2-c, w2-b)):
                e = h1 - a - b
                f = h2 - c - d
                g = w1 - a - c
                h = w2 - b - d
                if w3-e-f == h3-g-h > 0:
                    ans += 1
print(ans)
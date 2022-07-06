n, x = map(int, input().split())
pos = 0
game = []
ans = 4 * 10**18
for i in range(n):
    a, b = map(int, input().split())
    a += pos
    pos = 0
    if i >= x:continue
    ans = min(ans, a + b*(x-i))
    pos += a + b
print(ans)
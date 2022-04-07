n, q = map(int, input().split())
fields = [0] * (n + 2)
for i in range(q):
    l, r, x = map(int, input().split())
    fields[l] += x
    fields[r+1] -= x
now = 0
nxt = fields[1]
ans = []
for i in range(1, n):
    now += fields[i]
    nxt += fields[i+1]
    if now > nxt:
        ans.append('>')
    elif now < nxt:
        ans.append('<')
    else:
        ans.append('=')
print(''.join(ans))
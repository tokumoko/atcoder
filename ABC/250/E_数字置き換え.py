n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = dict()
val = 1
ans_a = [0] * n
ans_b = []
for i in range(n):
    if d.get(a[i], -1) == -1:
        d[a[i]] = val
        val += 1
    a[i] = d[a[i]]
for i in range(n):
    b[i] = d.get(b[i], 10**6)
val_a = 0
val_b = 0
st = set()
for i in range(n):
    val_a = max(val_a, a[i])
    ans_a[i] = val_a
    val_b = max(val_b, b[i])
    if not b[i] in st:
        st.add(b[i])
    ans_b.append((val_b, len(st)))
q = int(input())
for i in range(q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if ans_a[x] == ans_b[y][0] and ans_a[x] == ans_b[y][1]:
        print('Yes')
    else:
        print('No')
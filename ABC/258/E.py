n, q, x = map(int, input().split())
w = list(map(int, input().split()))
box = [0] * n
s = sum(w)
val = 0
cnt = 0
r = 0
for l in range(n):
    if x > s:
        val += x // s
        cnt += n
    while val < x:
        val += w[r]
        cnt += 1
        r += 1
        r %= n
    box[l] = cnt
    val -= w[l]
    cnt -= 1
p = set()
i = 0
glaph = []
while i not in p:
    glaph.append(i)
    p.add(i)
    i += box[i]
    i %= n
j = 0
while glaph[j] != i:
    j += 1
front = j
roop = len(glaph)-j
for i in range(q):
    k = int(input()) - 1
    if k < front:
        print(box[glaph[k]])
    else:
        k -= front
        print(box[glaph[front + k%roop]])
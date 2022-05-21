n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = set()
x = max(a)
for i in range(n):
    if a[i] == x:
        d.add(i+1)
flag = False
for i in range(k):
    if b[i] in d:
        flag = True
print('Yes' if flag else 'No')
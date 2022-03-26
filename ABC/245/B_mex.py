n = int(input())
a = list(map(int, input().split()))
a = list(set(a))
i = 0
while i == a[i]:
    i += 1
    if i == len(a):break
print(i)
n = int(input())
a = list(map(int, input().split()))
a.sort()
sa = a[0]
for i in range(1,n):
    sa += a[i] - a[i-1] + 1
if a[-1] - a[-2] > 1:
    print('Alice')
elif sa % 2 == 1:
    print('Alice')
else:
    print('Bob')
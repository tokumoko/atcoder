n = int(input())
a = list(map(int, input().split()))
k = 0
for i in range(4):
    k += a[n-i-1]
    if k >= 4:break
print(max(0, n-i))
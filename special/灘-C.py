n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 10 ** 18
for i in range(n):
    ans = min(ans, a[i] * b[i])
ans = min(ans, max(a) * min(b))
print(ans)
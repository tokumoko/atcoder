k = int(input())
ans = 90
for i in range(1,10**7+1):
    val = i * k
    res = 0
    while val >= 1:
        res += val % 10
        val //= 10
    ans = min(ans, res)
print(ans)
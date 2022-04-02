from math import pow
from math import floor
n = int(input())
if n == 0:
    print(0)
    exit()
a = floor(pow(n, 1/3))
ans = 10 ** 18
i = 0
while i < a:
    j = a-i
    while True:
        res = (i*i + j*j) * (i+j)
        j += 1
        a += 1
        if res >= n:
            a -= 1
            break
    ans = min(ans, res)
    i += 1
print(ans)
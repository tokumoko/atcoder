t = int(input())
n = int(input())
work = [0] * (t + 1)
for _ in range(n):
    l, r = map(int, input().split())
    work[l] += 1
    work[r] -= 1
now = 0
for i in range(t):
    now += work[i]
    print(now)
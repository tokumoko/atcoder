n, m, k = map(int, input().split())
w = [0] * n
dp = [[[0] * (n+3) for _ in range(n+3)] for _ in range(n+3)]
for i in range(n):
    w[i] = int(input())
sum_w = sum(w)

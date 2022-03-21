n = int(input())
flag = [True] * (2*n + 1)
i = 0
for i in range(n + 1):
    while not flag[i]:
        i += 1
    flag[i] = False
    i += 1
    print(i)
    t = int(input())
    flag[t - 1] = False
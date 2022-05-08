from math import sqrt
n = int(input())
A=[2]
for i in range(3, 793712, 2):
    brepo = sqrt(i)
    flag = True
    for j in A:
        if i % j == 0:
            flag = False
            break
        if j > brepo:
            break
    if flag:
        A.append(i)
        if 2 * i**3 > 10**18:
            break
l = len(A)
ans = 0
for i in range(l):
    flag = True
    for j in range(i+1, l):
        if A[i] * (A[j]**3) <= n:
            ans += 1
            flag = False
        else:
            break
    if flag:break
print(ans)
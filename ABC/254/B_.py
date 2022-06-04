n = int(input())
a = [1]
for i in range(1, n+1):
    b = [1]
    for j in range(i):
        if j == i-1:
            b.append(a[j])
        else:
            b.append(a[j] + a[j+1])
    print(*a)
    a = b
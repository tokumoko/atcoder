import math
a = []
for i in range(100):
    for j in range(i+1,100):
        n = (i*i + j*j) * (i+j)
        a.append((n, i, j))
print(sorted(a))
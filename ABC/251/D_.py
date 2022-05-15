a = []
for i in range(1, 100):
    a.append(i)
    a.append(i*100)
    a.append(i*10000)
a.sort()
a.append(1000000)
print(298)
print(*a)
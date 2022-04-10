n = int(input())
names = []
for i in range(n):
    s, t = map(str, input().split())
    names.append(s)
    names.append(t)
for i in range(n):
    family = names[i*2]
    first = names[i*2+1]
    flag1 = False
    flag2 = False
    for j in range(n):
        if i*2 == j or i*2+1 == j:pass
        if names[j] == family:
            flag1 = True
        if names[j] == first:
            flag2 = True
    if flag1 and flag2:
        print('No')
        exit()
print('Yes')
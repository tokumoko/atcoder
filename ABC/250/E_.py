n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sa = set()
sb = set()
anslist = set()
sa.add(a[0])
sb.add(b[0])
pa = [i for i in range(n)]
pb = [i for i in range(n)]
ax = 0
bx = 0
suma = a[0]
sumb = b[0]
for i in range(n):
    if a[i] in sa:
        pa[i] = ax
    else:
        for j in range(bx, n):
            if b[j] in sb:
                pb[j] = bx
            else:
                print(sa, sb)
                if suma == sumb:
                    anslist.add((ax, bx))
                sb.add(b[j])
                sumb += b[j]
                bx = j
                break
        sa.add(a[i])
        suma += a[i]
        ax = i
        print(ax, bx)
print(anslist)
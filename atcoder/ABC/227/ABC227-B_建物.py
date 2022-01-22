n=int(input())
a=list(map(int,input().split()))
s=[]
for c in range(1,150):
    for b in range(1,150):
        b=int(4*c*b+3*c+3*b)
        if b<1000:
            s.append(b)
print(sorted(set(s)))
m=0
for i in range(n):
    if a[i] not in s:
        m+=1
print(m)
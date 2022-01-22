n=int(input())
a=list(map(int, input().split()))
c=0
q=0
kati=0
while True:
    for i in range(n):
        m=0
        for j in range(n-1):
            if j==i:
                continue
            else :
                m=m ^ a[j]
        if m==0: 
            break
    if m==0:
        break
    else :
        del a[0]
        n-=1
        kati+=1
print('Win' if kati%2==0 else 'Lose')
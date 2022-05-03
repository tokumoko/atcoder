N=int(input())
a=[0]*N
b=[i for i in range(1,N+1)]
for i in range(N):
    a[i]=int(input())
k=sum(b)-sum(a)
a=list(set(a))
if a==b:
    print('Correct')
else:
    a.append(0)
    i=0
    while b[i]==a[i]:
        i+=1
    print(i+1-k,i+1)
from math import sqrt
def soin(N):
    a=[]
    while N!=1:
        flag=True
        for i in range(2,int(sqrt(N))+1):
            while N%i==0:
                a.append(i)
                N//=i
                flag=False
        if flag:
            a.append(N)
            break
    return a
def kobai(a,b):
    for i in a:
        if b%i==0:b//=i
    if b!=1:
        a+=soin(b)
    return a
N=int(input())
A=list(map(int,input().split()))
A.sort(reverse=True)
ans=1
k=soin(A[0])
for i in range(1,N):
    k=kobai(k,A[i])
for i in k:ans*=i
print(ans)
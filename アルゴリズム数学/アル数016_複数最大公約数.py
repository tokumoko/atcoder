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
N=int(input())
A=list(map(int,input().split()))
a=soin(min(A))
for i in range(1,N):
    b=[]
    for j in range(len(a)):
        if A[i]%a[j]==0:
            A[i]//=a[j]
            b.append(a[j])
    a=b
    if len(a)==0:
        print(1)
        exit()
ans=1
for i in a:ans*=i
print(ans)
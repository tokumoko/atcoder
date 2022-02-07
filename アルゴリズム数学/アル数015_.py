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

A,B=map(int,input().split())
ans1=soin(A)
ans2=soin(B)
j=0
k=0
ans=1
while(1):
    if ans1[j]==ans2[k]:
        ans*=ans1[j]
        j+=1
        k+=1
    elif ans1[j]>ans2[k]:
        k+=1
    else:
        j+=1
    if j==len(ans1) or k==len(ans2):break
print(ans)
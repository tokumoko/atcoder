
def cut(x):
    s=0
    count=0
    for b in B:
        s+=b
        if s>=x:
            count+=1
            s=0
    return count>=K+1

N,L=map(int,input().split())
K=int(input())
A=[0]+list(map(int,input().split()))+[L]
B=[A[i+1]-A[i] for i in range(N+1)]

left=0
right=L
while abs(right-left)>1:
    mid=(right+left)//2
    if cut(mid):left=mid
    else:right=mid
print(left)
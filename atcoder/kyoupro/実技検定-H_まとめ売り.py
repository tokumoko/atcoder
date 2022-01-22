def tanpin(x,a):
    global ans
    global oddmin
    global totalmin
    global totalgen
    global oddgen
    x-=1
    if x%2==0:
        if (C[x]-oddgen)>=a:
            C[x]-=a
            oddmin=min(oddmin,C[x])
            totalmin=min(totalmin,C[x])
            ans+=a
    else:
        if (C[x]-totalgen)>=a:
            C[x]-=a
            totalmin=min(totalmin,C[x])
            ans+=a
    return

def setto(a):
    global ans
    global oddmin
    global totalmin
    global totalgen
    global oddgen
    if oddmin>=a:
        oddgen+=a
        ans+=((N+1)//2)*a
        oddmin-=a
        totalmin=min(oddmin,totalmin)
    return
    
def zenshurui(a):
    global ans
    global oddmin
    global totalmin
    global totalgen
    global oddgen
    if totalmin>=a:
        totalgen+=a
        oddgen+=a
        ans+=N*a
        totalmin-=a
        oddmin-=a
    return

N=int(input())
C=list(map(int,input().split()))
Q=int(input())
ans=0
totalmin=min(C)
oddmin=10**10
totalgen=0
oddgen=0
for i in range(0,N,2):
    if oddmin>C[i]:oddmin=C[i]
for _ in range(Q):
    S=list(map(int,input().split()))
    if S[0]==1:
        tanpin(S[1],S[2])
    elif S[0]==2:
        setto(S[1])
    elif S[0]==3:
        zenshurui(S[1])
    
print(int(ans))
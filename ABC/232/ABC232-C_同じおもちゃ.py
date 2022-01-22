N,M=map(int,input().split())
P=[0]*N
Q=[0]*N
for i in range(M):
    A,B=map(int,input().split())
    A-=1
    B-=1
    P[A]+=1
    P[B]+=1
for i in range(M):
    A,B=map(int,input().split())
    A-=1
    B-=1
    Q[A]+=1
    Q[B]+=1
if sorted(P)==sorted(Q):
    print("Yes")
else :
    print("No")
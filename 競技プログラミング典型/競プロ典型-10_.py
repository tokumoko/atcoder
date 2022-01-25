N=int(input())
score1=[0]*N;score2=[0]*N
for i in range(N):
    C,P=map(int,input().split())
    if C==1:
        score1[i]=score1[i-1]+P
        score2[i]=score2[i-1]
    else:
        score1[i]=score1[i-1]
        score2[i]=score2[i-1]+P
Q=int(input())
for i in range(Q):
    L,R=map(int,input().split())
    L-=1;R-=1
    if L!=0:print(score1[R]-score1[L-1],score2[R]-score2[L-1])
    else:print(score1[R],score2[R])
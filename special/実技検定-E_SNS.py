def fl(x,y):
    S[x-1][y-1]='Y'
    return

def flgaesi(x):
    for i in range(N):
        if S[i][x-1]=='Y':
            S[x-1][i]='Y'
    return

def flfl(x):
    A=[]
    for i in range(N):
        if S[x-1][i]=='Y':
            A.append(i)
    for i in A:
        for j in range(N):
            if j==x-1: continue
            if S[i][j]=='Y':
                S[x-1][j]='Y'
    return

import numpy as np
N,Q=map(int,input().split())
S=np.array([['N']*N]*N)
A=[]
for _ in range(Q):
    A=list(map(int,input().split()))
    if A[0]==1:
        fl(A[1],A[2])
    elif A[0]==2:
        flgaesi(A[1])
    else :
        flfl(A[1])
for i in range(N):
    for j in range(N):
        print(S[i][j],end="")
    print("")
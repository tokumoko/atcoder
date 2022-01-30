H,W=map(int,input().split())
B=[[0]*H for _ in range(W)]
for i in range(H):
    A=list(map(str,input().split()))
    for j in range(W):
        B[j][i]=A[j]
for i in range(W):
    print(' '.join(B[i]))
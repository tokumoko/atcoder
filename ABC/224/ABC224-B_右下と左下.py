H,W=map(int,input().split())
A=[0]*H
for i in range(H):
    A[i]=list(map(int,input().split()))
ans=True
for i in range(H-1):
    for j in range(W-1):
        for k in range(i+1,H):
            for l in range(j+1,W):
                if A[i][j]+A[k][l]>A[i][l]+A[k][j]:ans=False
print("Yes" if ans else "No")
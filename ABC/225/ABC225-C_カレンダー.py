N,M=map(int,input().split())
A=[0]*N
for i in range(N):
    B=list(map(int, input().split()))
    for j in range(M-1):
        if B[j+1]!=B[j]+1 or B[j]%7==0:
            print("No")
            exit()
    A[i]=B[0]
for i in range(N-1):
    if A[i+1]!=A[i]+7:
        print("No")
        exit()
print("Yes")
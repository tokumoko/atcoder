import bisect
N=int(input())
S=0
D=[0]*N
A=[0]*N
B=[0]*N
a=0
for i in range(N):
    A[i],B[i]=map(int,input().split())
    k=A[i]/B[i]
    D[i]=D[i-1]+k
    S+=k
if N==1:
    print(A[0]/2)
    exit()
S/=2
n=bisect.bisect(D,S)
k=S-D[n-1]
print(sum(A[:n])+k*B[n])
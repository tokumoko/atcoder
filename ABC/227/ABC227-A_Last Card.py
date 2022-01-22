N,K,A=map(int,input().split())
a=K%N
A=A+a-1
if A==0:
    print(N)
elif A<=N:
    print(A)
else :
    print(A%N)
N=int(input())
A=list(map(int,input().split()))
sum=0
B=[0]*(N+2)
for i in range(N):
    sum+=A[i]
    sum%=360
    B[i]=sum
B[N]=360
B.sort(reverse=True)
max=0
for i in range(N+1):
    score=B[i]-B[i+1]
    if max<score:max=score
print(max)
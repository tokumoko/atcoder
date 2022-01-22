def state(x): #習得すべき技に1を代入
    for i in x:
        waza[i-1]=1
    return

N=int(input())
time=0
waza=[0]*N #習得してる技
A=[[]]*N
for i in range(N):
    A[i]=list(map(int,input().split()))
waza[N-1]=1
for i in range(N-1,0,-1):
    if waza[i]:
        state(A[i][2:])

for i in range(N):
    if waza[i]==1: time+=A[i][0]
print(time)
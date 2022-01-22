import math
N=int(input())
x=[0]*N
y=[0]*N
max=0
for i in range(N):
    x[i],y[i]=map(int,input().split())
for i in range(N-1):
    for j in range(i,N):
        ans=(x[j]-x[i])*(x[j]-x[i])+(y[j]-y[i])*(y[j]-y[i])
        if max<ans:
            max=ans
print(math.sqrt(max))
from collections import deque
a,N=map(int,input().split())
M=1
while M<=N:M*=10
d=[-1]*M
Q=deque()
d[1]=0
Q.append(1)

while len(Q):
    c=Q.popleft
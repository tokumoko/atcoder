N=int(input())
XY=[0]*N
for i in range(N):
    XY[i]=list(map(int,input().split()))
count=0
for i in range(N-2):
    for j in range(i,N-1):
        A=XY[j][0]-XY[i][0]
        B=XY[j][1]-XY[i][1]
        for k in range(j,N):
            if A*(XY[k][1]-XY[i][1])-(XY[k][0]-XY[i][0])*B!=0:count+=1
print(count)
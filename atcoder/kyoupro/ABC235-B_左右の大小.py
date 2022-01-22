N=int(input())
H=list(map(int,input().split()))
i=0
flag=False
for i in range(N-1):
    if H[i]>=H[i+1]:
        flag=True
        break
if flag:print(H[i])
else:print(H[i+1])
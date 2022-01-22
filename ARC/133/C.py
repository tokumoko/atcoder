H,W,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
if sum(A)%K!=sum(B)%K:
    print(-1)
    exit()
res=[0]*K
ans1=0
ans2=0
for i in range(H*(K-1),H*(K-1)-K,-1):res[i%K]=i
for i in B:ans1+=res[i]
for i in range(W*(K-1),W*(K-1)-K,-1):res[i%K]=i
for i in A:ans2+=res[i]
print(min(ans1,ans2))
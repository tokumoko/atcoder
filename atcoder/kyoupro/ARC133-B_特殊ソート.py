n=int(input())
p=list(map(int,input().split()))
idx=p.index(1)
ans1=idx
ans2=len(p)-idx
if p[(idx+1)%len(p)]==2:ans2+=2
else :ans1+=2
print(min(ans1,ans2))
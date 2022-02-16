n=int(input())
a=list(map(int,input().split()))
cards=[0,0,0]
for i in a:cards[i-1]+=1
ans=0
for i in cards:ans+=i*(i-1)//2
print(ans)
N,Q=map(int,input().split())
A=[(a,10**9) for a in map(int,input().split())]
print(A)
X=[]
for i in range(Q):
  x=int(input())
  X.append((x,i))
print(X)

AX=sorted(A+X)[::-1]
print(AX)

ans=[0]*Q
cnt=0
for x,i in AX:
  print(x,i)
  print(i,Q)
  if i<Q:
    ans[i]=cnt
  else:
    cnt+=1

print(*ans,sep="\n")
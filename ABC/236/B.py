N=int(input())
A=list(map(int,input().split()))
k=[0]*(N+1)
for i in A:k[i]+=1
print(k.index(3))
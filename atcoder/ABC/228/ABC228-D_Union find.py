Q=int(input())
N=2**20
A=[-1]*N
P=list(range(N))
 
def find(x):
	if x==P[x]: return x
	P[x] = find(P[x])
	return P[x]
 
for _ in range(Q):
	t,x = map(int,input().split())
	if t==1:
		i = find(x%N)
		A[i] = x
		P[i] = find( (i+1)%N )
	else:
		print(A[x%N])
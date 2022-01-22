K,N=map(int,input().split())
S=list(input())
ans=[]
T=[0]*K
ind=0
for i in range(K):T[i]=ord(S[i])
for i in range(N):
    ans.append(min(T[ind:K-N+1]))
    ind=T.index(ans[i])
    del T[ind]
for i in range(N):print(chr(ans[i]),end='')
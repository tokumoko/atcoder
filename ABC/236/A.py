S=list(input())
a,b=map(int,input().split())
s=S[a-1]
S[a-1]=S[b-1]
S[b-1]=s
print(''.join(S))
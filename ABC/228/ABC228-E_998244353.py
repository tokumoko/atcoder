N,K,M = map(int, input().split())
A=998244353
if M%A==0:
    print(0)
    exit()
r=pow(K,N,A-1)
print(pow(M,r,A))
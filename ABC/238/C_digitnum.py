def tousa(n):
    return (1+n)*n//2

N=list(input())
l=len(N)
N=int(''.join(N))
A=998244353
sum=0
for i in range(l-1):
    k=9*(10**i)
    sum+=tousa(k)
    sum%=998244353
k=10**(l-1)
N-=k-1
sum+=tousa(N)
sum%=998244353
print(sum)
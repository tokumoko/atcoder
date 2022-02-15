N=int(input())
MOD=10**9+7
a=2**N-1
l=[1]
for i in range(1,200001):
    l.append(i*l[i-1]%MOD)
m=[]
for i in range(200001):
    m.append(pow(l[i],MOD-2,MOD))
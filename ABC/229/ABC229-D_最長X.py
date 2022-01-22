n=input()
k=int(input())
ans=0
a=[i for i in range(len(n)) if n[i]=='.']
a.insert(0,-1)
a.append(len(n))
b=[a[i+1]-a[i]-1 for i in range(len(a)-1)]
c=[sum(b[i:i+k+1]) for i in range(max(1,len(b)-k))]
print(max(c)+min(k,len(b)-1))
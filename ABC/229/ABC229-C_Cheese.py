n,w = map(int,input().split())
a=[];b=[]
s=0;r=0;j=0;m=0
for i in range(n):
    c,d=map(int,input().split())
    a.append(c)
    b.append(d)
zip_list=zip(a,b)
zip_sort=sorted(zip_list,reverse=True)
a,b=zip(*zip_sort)
while j<n:
    r+=a[j]*min(b[j],w-s)
    s+=min(b[j],w-s)
    j+=1
print(r)
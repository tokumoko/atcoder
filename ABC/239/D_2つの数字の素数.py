from math import sqrt
a,b,c,d=map(int,input().split())
for i in range(a,b+1):
    ans=True
    for j in range(c,d+1):
        flag=True
        for k in range(2,int(sqrt(i+j))+1):
            if (i+j)%k==0:flag=False
        if flag:ans=False
    if ans:break
print('Takahashi' if ans else 'Aoki')
import itertools

N=int(input())
a=[[0]]*(N-1)
p=[1,2,3]
max=-10**100
for i in range(N-1):
    a[i]=list(map(int,input().split()))
for s in itertools.product(p,repeat=N):#順列全列挙
    X=[];Y=[];Z=[];ans=0
    if s[0]!=1:break#1番目は1のときだけでよい(2とか3を入れても結果は変わらん)
    for i in range(N):
        if s[i]==1:
            for j in X:
                ans+=a[j][i-j-1]
            X.append(i)
        elif s[i]==2:
            for j in Y:
                ans+=a[j][i-j-1]
            Y.append(i)
        elif s[i]==3:
            for j in Z:
                ans+=a[j][i-j-1]
            Z.append(i)
    if max<ans:
        max=ans
print(max)
n=int(input())
a=list(map(int,input().split()))
k=0 #ボールの個数
o=[0] #前回のボール
m=[] #連続の回数
for i in range(n):
    k+=1
    if a[i]==o[-1]:
        m[-1]+=1
        if m[-1]==o[-1]:
            k-=m[-1]
            del o[-1]
            del m[-1]
    else:
        o.append(a[i])
        m.append(1)
    print(k)
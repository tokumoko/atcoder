a=[]
K=int(input())
while K>0:
    if K%2==1:a.append(str(2))
    else :a.append(str(0))
    K//=2
a.reverse()
s = ''.join(a)
print(s)
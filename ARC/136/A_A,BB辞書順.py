from sys import flags


n=int(input())
s=list(input())
t=[0]*(n*2)
k=0
for i in range(n):
    if s[i]=='A':
        t[k]=1
        t[k+1]=1
        k+=1
    elif s[i]=='B':
        t[k]=1
    else:
        t[k]=2
    k+=1
ans=[]
flag=False
for i in range(n*2):
    if flag:
        flag=False
        continue
    if t[i]==1 and i!=n*2-1:
        if t[i+1]==1:
            ans.append('A')
            flag=True
        else:
            ans.append('B')
    elif t[i]==2:
        ans.append('C')
    else:
        break
print(''.join(ans))
s=input()
m=0
a=0
n=0
for i in range(len(s)):
    if s[i]=='o' and n==2 and i>=2:
        n=0
    elif s[i]=='x' and n<2:
        n+=1
    elif i==0 and s[i]=='o':
        n=0
    elif i==1 and s[i]=='o' and n==1:
        n=0
    else : 
        m=1
        break
if m==0:
    print('Yes')
else:
    print('No')
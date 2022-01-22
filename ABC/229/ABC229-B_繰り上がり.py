a,b=input().split()
k=0
i=1
s=0
while len(a)>=i and len(b)>=i:
    if int(a[-i])+int(b[-i])>=10:
        s+=1
    i+=1
print('Easy' if s==0 else 'Hard')
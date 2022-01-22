S=list(input())
ans=[];N=[]
count=0
for i in range(len(S)):
    if S[i].isupper():
        count+=1
        if count==1:
            a=i
        else:
            spell=''.join(S[a:i+1])
            ans.append(spell)
            count=0
N=sorted(ans,key=str.lower)
for i in range(len(N)):
    print(N[i],end="")
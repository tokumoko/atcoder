S=list(input())
l=0
r=len(S)
while S[l]=='a':
    l+=1
    if l==r:
        print('Yes')
        exit()
r-=1
while S[r]=='a':
    r-=1
if l>(len(S)-r-1):
    print('No')
    exit()
flag=True
for i in range(l,r):
    if S[i]!=S[r]:flag=False
    r-=1
print('Yes' if flag else 'No')
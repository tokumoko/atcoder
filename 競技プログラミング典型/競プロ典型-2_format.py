N=int(input())
if N%2==1:exit()
for i in range(2**(N)-2,2**(N-1)-2,-2):
    b='{:b}'.format(i)
    count=0
    ans=''
    flag=True
    for j in range(N):
        if b[j]=='1':
            ans+='('
            count+=1
        else:
            ans+=')'
            count-=1
        if count<0:flag=False
    if count==0 and flag:print(ans)
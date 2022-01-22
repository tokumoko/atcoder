s,t,x=map(int,input().split())
if s<t:
    if s<=x and x<t:
        ans='Yes'
    else : ans='No'
else :
    if s<=x or t>x:
        ans='Yes'
    else : ans='No'
print(ans)
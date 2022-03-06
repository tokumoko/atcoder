from math import ceil
t=int(input())
A=65
mod=998244353
ans=[]
for i in range(t):
    n=int(input())
    s=list(input())
    if n==1:
        ans.append(ord(s[0])-A+1)
        continue
    score=0
    halfn=ceil(n/2)
    c=1
    for j in range(halfn):
        score*=26
        score+=ord(s[j])-A
        score%=mod
    right=halfn
    left=halfn-1
    if n%2==1:left-=1
    while s[left]==s[right]:
        if left==0:break
        left-=1
        right+=1
    if s[left]<=s[right]:
        score+=1
        score%=mod
    ans.append(score)
for i in ans:print(i)
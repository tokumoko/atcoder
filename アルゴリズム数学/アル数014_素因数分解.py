from math import sqrt
N=int(input())
a=[]
while N!=1:
    count=0
    for i in range(2,int(sqrt(N))+1):
        while N%i==0:
            a.append(i)
            N//=i
            count+=1
    if count==0:
        a.append(N)
        break
print(*a)
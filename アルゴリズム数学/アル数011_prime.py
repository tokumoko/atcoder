N=int(input())
A=[]
for i in range(2,N+1):
    flag=True
    for j in A:
        if i%j==0:flag=False
    if flag:A.append(i)
print(*A)
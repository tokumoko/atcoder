from math import sqrt
N=int(input())
flag=True
for i in range(2,int(sqrt(N))+1):
    if N%i==0:flag=False
print('Yes' if flag else 'No')
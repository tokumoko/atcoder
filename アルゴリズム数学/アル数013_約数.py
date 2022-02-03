from math import sqrt
N=int(input())
for i in range(1,int(sqrt(N))+1):
    if N%i==0:
        print(i)
        if N//i!=i:print(N//i)
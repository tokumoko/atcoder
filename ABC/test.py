import math
a=10**18
n=0
while a>1:
    a/=2
    n+=1
print(n)
print(math.log(10**18,2))
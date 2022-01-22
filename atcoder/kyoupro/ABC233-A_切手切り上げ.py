import math
A,B=map(int,input().split())
print(max(math.ceil((B-A)/10),0))
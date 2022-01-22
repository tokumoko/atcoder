import math
import itertools
N=int(input())
XY=[[] for _ in range(N)]
for i in range(N):XY[i]=list(map(int,input().split()))
for p in itertools.permutations(XY,repeat=3):
    print(p)
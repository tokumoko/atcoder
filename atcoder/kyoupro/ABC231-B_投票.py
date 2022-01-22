import collections


N=int(input())
s=[0]*N
for i in range(N):
    s[i]=input()
c = collections.Counter(s)
print(c.most_common()[0][0])
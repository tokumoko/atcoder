import bisect
def query1(x):
    

q=int(input())

for i in range(q):
    a=list(map(int,input().split()))
    if a[0]==1:query1(a[1])
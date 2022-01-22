n,k=map(int, input().split())
test=[]
for i in range(n):
    a,b,c=map(int,input().split())
    test.append(a+b+c)
list=sorted(test,reverse=True)
a=list[k-1]-300
for i in test:
    print('Yes' if i>=a else 'No')
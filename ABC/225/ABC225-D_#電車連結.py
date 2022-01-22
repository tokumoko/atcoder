N,M=map(int,input().split())
P=[i+1 for i in range(N)]
Q=[i+1 for i in range(N)]
def renketsu(x,y):
    P[y-1]=x
    Q[x-1]=y
def bunnri(x,y):
    P[y-1]=y
    Q[x-1]=x
def sentou(x):
    if P[x-1]==x:return x
    else:return sentou(P[x-1])
def ans(x):
    a.append(x)
    if Q[x-1]==x:
        return
    else :
        ans(Q[x-1])
        return
    
for i in range(M):
    query=list(map(int, input().split()))
    if query[0]==1:
        renketsu(query[1],query[2])
    elif query[0]==2:
        bunnri(query[1],query[2])
    else:
        a=[]
        k=sentou(query[1])
        ans(k)
        print(len(a),end=" ")
        for z in a:
            print(z,end=" ")
        print("")
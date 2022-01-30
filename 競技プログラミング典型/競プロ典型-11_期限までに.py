N=int(input())
dp=[[] for _ in range(20)]
D=[0]*N;C=[0]*N;S=[0]*N
for i in range(N):
    D[i],C[i],S[i]=map(int,input().split())
zip_list=zip(D,C,S)
zip_sort=sorted(zip_list)
D,C,S=zip(*zip_sort)
ans=0
for i in range(2**N):
    b='{:b}'.format(i)
    b=b.zfill(N)
    score=0
    day=0
    flag=True
    for j in range(N):
        if b[j]=='1':
            day+=C[j]
            score+=S[j]
            if day>D[j]:flag=False
    if flag:ans=max(ans,score)
print(ans)
def yoko(a,b):
    score=0
    for i in range(b,b+6):
        if s[a][i]=='#':score+=1
    if score>=4:return True
    return False
def tate(a,b):
    score=0
    for i in range(a,a+6):
        if s[i][b]=='#':score+=1
    if score>=4:return True
    return False
def naname(a,b):
    score=0
    for i in range(6):
        if s[a+i][b+i]=='#':score+=1
    if score>=4:return True
    return False
def nanameme(a,b):
    score=0
    for i in range(6):
        if s[a+i][b-i]=='#':score+=1
    if score>=4:return True
    return False

n=int(input())
s=[[] for _ in range(n)]
for i in range(n):
    s[i]=list(input())
for i in range(n):
    for j in range(n):
        flag1=False
        flag2=False
        flag3=False
        flag4=False
        if i<=n-6:flag1=tate(i,j)
        if j<=n-6:flag2=yoko(i,j)
        if i<=n-6 and j<=n-6:flag3=naname(i,j)
        if i<=n-6 and j>=5:flag4=nanameme(i,j)
        if flag1 or flag2 or flag3 or flag4:
            print('Yes')
            exit()
print('No')
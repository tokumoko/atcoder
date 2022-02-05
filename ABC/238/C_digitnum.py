a=[[0]*10 for _ in range(17)]
for i in range(17):
    for j in range(1,10):
        if j==1:
            a[i][j]=1
        elif j==2:
            if i==0:
                a[i][j]=3
            else:
                a[i][j]=a[i-1][9]+2*10**(i)+1
        else:
            if i==0:
                a[i][j]=a[i][j-1]+j
            else:
                a[i][j]=a[i][2]+(10**(i+1))*(j-2)+a[i][j-1]-1
print(a)
N=int(input())
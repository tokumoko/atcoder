def flag(ind1, ind2):
    if s[ind1] == 'R' and s[ind2] == 'L':
        return True
    else:
        return False

n = int(input())
z = []
for i in range(n):
    x, y = map(int,input().split())
    z.append((y,x,i))
s = list(input())
z.sort()
for i in range(n-1):
    if z[i][0] == z[i+1][0]:
        if flag(z[i][2],z[i+1][2]):
            print('Yes')
            exit()
print('No')
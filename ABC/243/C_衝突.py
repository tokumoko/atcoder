n = int(input())
z = []
for i in range(n):
    x, y = map(int,input().split())
    z.append((y,x,i))
s = list(input())
z.sort()
for i in range(n-1):
    if z[i][0] == z[i+1][0]:
        if s[z[i][2]] == 'R' and s[z[i+1][2]] == 'L':
            print('Yes')
            exit()
print('No')
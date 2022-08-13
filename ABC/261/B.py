n = int(input())
a = [list(input()) for _ in range(n)]
flag = True
for i in range(n):
    for j in range(n):
        if i == j:continue
        if a[i][j] == 'W' and a[j][i] == 'L' or \
           a[i][j] == 'D' and a[j][i] == 'D' or \
           a[i][j] == 'L' and a[j][i] == 'W':
               continue
        else:
            flag = False
print('correct' if flag else 'incorrect')
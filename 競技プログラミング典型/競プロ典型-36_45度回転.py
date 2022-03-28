n, q = map(int, input().split())
a = [0] * n
b = [0] * n
x, y = map(int, input().split())
max_x = [x+y, x-y, x-y]
min_x = [x+y, x-y, x-y]
max_y = [x-y, x+y, x+y]
min_y = [x-y, x+y, x+y]
a[0] = x
b[0] = y
for i in range(1,n):
    x, y = map(int, input().split())
    if x+y > max_x[0]:
        max_x = [x+y, x-y, x-y]
    elif x+y == max_x[0]:
        max_x[1] = max(max_x[1], x-y)
        max_x[2] = min(max_x[2], x-y)
    if x+y < min_x[0]:
        min_x = [x+y, x-y, x-y]
    elif x+y == min_x[0]:
        min_x[1] = max(min_x[1], x-y)
        min_x[2] = min(min_x[2], x-y)
    if x-y > max_y[0]:
        max_y = [x-y, x+y, x+y]
    elif x-y == max_y[0]:
        max_y[1] = max(max_y[1], x+y)
        max_y[2] = min(max_y[2], x+y)
    if x-y < min_y[0]:
        min_y = [x-y, x+y, x+y]
    elif x-y == min_y[0]:
        min_y[1] = max(min_y[1], x+y)
        min_y[2] = min(min_y[2], x+y)
    a[i] = x
    b[i] = y
mht = [ ((max_x[0]+max_x[1])//2,(max_x[0]-max_x[1])//2),\
        ((max_x[0]+max_x[2])//2,(max_x[0]-max_x[2])//2),\
        ((min_x[0]+min_x[1])//2,(min_x[0]-min_x[1])//2),\
        ((min_x[0]+min_x[2])//2,(min_x[0]-min_x[2])//2),\
        ((max_y[0]+max_y[1])//2,(max_y[1]-max_y[0])//2),\
        ((max_y[0]+max_y[2])//2,(max_y[2]-max_y[0])//2),\
        ((min_y[0]+min_y[1])//2,(min_y[1]-min_y[0])//2),\
        ((min_y[0]+min_y[2])//2,(min_y[2]-min_y[0])//2)]
mht = set(mht)
for i in range(q):
    que = int(input())
    que -= 1
    x = a[que]
    y = b[que]
    ans = 0
    for i, j in mht:
        ans = max(ans, (abs(x-i) + abs(y-j)))
    print(ans)
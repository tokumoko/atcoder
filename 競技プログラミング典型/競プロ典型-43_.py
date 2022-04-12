def go(x, y):
    que = [(x, y, -1, -1, 0, -1)]
    while len(que) != 0:
        x, y, posx, posy, drc, val = que.pop(0)
        if maze[x][y] < val:continue
        else:maze[x][y] = val
        if x == gr and y == gc:continue
        if x > 0 and x-1 != posx and maze[x-1][y] != -1:
            if drc == 1:
                que.append((x-1, y, x, y, 1, val))
            else:
                que.append((x-1, y, x, y, 1, val+1))
        if y > 0 and y-1 != posy and maze[x][y-1] != -1:
            if drc == 2:
                que.append((x, y-1, x, y, 2, val))
            else:
                que.append((x, y-1, x, y, 2, val+1))
        if x < h-1 and x+1 != posx and maze[x+1][y] != -1:
            if drc == 3:
                que.append((x+1, y, x, y, 3, val))
            else:
                que.append((x+1, y, x, y, 3, val+1))
        if y < w-1 and y+1 != posy and maze[x][y+1] != -1:
            if drc == 4:
                que.append((x, y+1, x, y, 4, val))
            else:
                que.append((x, y+1, x, y, 4, val+1))
    return

h, w = map(int, input().split())
sr, sc = map(int, input().split())
gr, gc = map(int, input().split())
sr -= 1;sc -= 1;gr -= 1;gc -= 1
s = [list(input()) for _ in range(h)]
maze = [[10**9] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            maze[i][j] = -1
go(sr, sc)
print(maze[gr][gc])
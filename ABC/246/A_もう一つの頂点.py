x = [0] * 3
y = [0] * 3
for i in range(3):
    x[i], y[i] = map(int, input().split())
for i in range(3):
    if x[0] == x[1]:ansx = x[2]
    elif x[2] == x[1]:ansx = x[0]
    elif x[0] == x[2]:ansx = x[1]
    if y[0] == y[1]:ansy = y[2]
    elif y[2] == y[1]:ansy = y[0]
    elif y[0] == y[2]:ansy = y[1]
print(ansx, ansy)
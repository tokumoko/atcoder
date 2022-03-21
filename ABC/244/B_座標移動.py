n = int(input())
t = input()
tx = 0
ty = 0
x = 1
y = 0
for i in t:
    if i == 'S':
        tx += x
        ty += y
    else:
        if x == 1:
            x = 0
            y = -1
        elif y == -1:
            x = -1
            y = 0
        elif x == -1:
            x = 0
            y = 1
        else:
            x = 1
            y = 0
print(tx,ty)
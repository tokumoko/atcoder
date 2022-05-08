n, a, b = map(int, input().split())
tairu = [["."] * (n*b) for _ in range(n*a)]
for i in range(n*a):
    x = i // a
    if x % 2 == 0:
        flag1 = False
    else:
        flag1 = True
    for j in range(n*b):
        y = j // b
        if y % 2 == 0:
            flag2 = False
        else:
            flag2 = True
        if flag1^flag2:
            tairu[i][j] = '#'
for i in range(n*a):
    print(''.join(tairu[i]))
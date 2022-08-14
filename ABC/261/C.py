n = int(input())
d = dict()
for i in range(n):
    s = input()
    if d.get(s, 0) == 0:
        d[s] = 0
        print(s)
    else:
        print(s + '(' + str(d[s]) + ')')
    d[s] += 1
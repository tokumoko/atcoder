s = list(input())
a = [True] * 10
for i in range(9):
    a[int(s[i])] = False
for i in range(10):
    if a[i]:
        print(i)
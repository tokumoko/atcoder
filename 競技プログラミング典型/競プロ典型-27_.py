n = int(input())
d = {}
for i in range(1,n+1):
    s = input()
    flag = d.get(s,True)
    d[s] = False
    if flag:
        print(i)
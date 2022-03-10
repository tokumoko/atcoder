n,b=map(int,input().split())

def f(x):
    seki = 1
    for char in str(x):
        seki *= int(char)
    return seki

ans=0
for seven in range(12):
    for five in range(12):
        for three in range(23):
            for two in range(34):
                fm = (2**two) * (3**three) * (5**five) * (7**seven)
                m = fm + b
                if m > n:break
                if f(m) == fm:
                    ans+=1
if f(b) == 0 and b<=n:ans+=1
print(ans)
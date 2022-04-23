a, b, c, d, e, f, x = map(int, input().split())
taka = ((x // (a+c))*a + min(a, x % (a+c))) * b
aoki = ((x // (d+f))*d + min(d, x % (d+f))) * e
if taka > aoki:
    print('Takahashi')
elif taka < aoki:
    print('Aoki')
else:
    print('Draw')
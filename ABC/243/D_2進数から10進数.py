n, x = map(int, input().split())
s = list(input())
b = '{:b}'.format(x)
b = list(b)
for i in range(n):
    if s[i] == 'U':
        del b[-1]
    elif s[i] == 'R':
        b.append('1')
    else:
        b.append('0')
print(int(''.join(b),2))
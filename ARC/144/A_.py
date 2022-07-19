n = int(input())
l = []
if n % 4 != 0:
    x = n%4
    l.append(str(x))
for _ in range(n//4):
    l.append(str(4))
print(2*n)
print(''.join(l))
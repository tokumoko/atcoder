n = int(input())
m = 1
while n > m:
    m = m*2 + 1
if n == m:
    print('Second')
else:
    print('First')
n = int(input())
a = list(map(int, input().split()))
#コーナーケース
if a[0] == 1:
    print('No')
    exit()
if n == 1 and a[0] == 0:
    print('Yes')
    exit()

for i in range(n-1):
    if a[i] == a[i+1]:
        break
flip = i
x = 0
for j in range(n-1, i, -1):
    if a[j] != x:
        if x == 0:x = 1
        else:x = 0
        flip -= 1
if flip < 0:
    print('No')
else:
    print('Yes')
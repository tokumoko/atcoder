n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
student = [False] * n
a_n = []
b_n = []
ab_n = []
for i in range(n):
    a_n.append((a[i], n-i-1))
    b_n.append((b[i], n-i-1))
    ab_n.append((a[i] + b[i], n-i-1))
a_n.sort(reverse=True)
b_n.sort(reverse=True)
ab_n.sort(reverse=True)
i = 0
while i < x:
    student[a_n[i][1]] = True
    i += 1
i = 0
while i < y:
    if student[b_n[i][1]]:
        y += 1
    else:
        student[b_n[i][1]] = True
    i += 1
i = 0
while i < z:
    if student[ab_n[i][1]]:
        z += 1
    else:
        student[ab_n[i][1]] = True
    i += 1
student.reverse()
for i in range(n):
    if student[i]:
        print(i+1)
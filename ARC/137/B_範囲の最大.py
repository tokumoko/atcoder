n = int(input())
a = list(map(int, input().split()))
one = 0
zero = 0
max_zero = 0
max_one = 0
for i in range(n):
    if a[i] == 0:
        zero += 1
        one -= 1
        one = max(one,0)
    elif a[i] == 1:
        one += 1
        zero -= 1
        zero = max(zero,0)
    max_zero = max(max_zero, zero)
    max_one = max(max_one, one)
print(max_zero + max_one + 1)
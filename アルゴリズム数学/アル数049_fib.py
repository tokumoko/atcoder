n = int(input())
a = 1
b = 1
mod = 10**9 + 7
for i in range(n-2):
    tmp = a
    a += b
    a %= mod
    b = tmp
print(a)
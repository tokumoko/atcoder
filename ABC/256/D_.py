n = int(input())
a = [0] * ((2 * 10**5)+1)
for i in range(n):
    l, r = map(int, input().split())
    a[l] += 1
    a[r] -= 1
val = 0
st = -1
for i in range((2 * 10**5)+1):
    val += a[i]
    if val > 0 and st == -1:
        st = i
    if val == 0 and st != -1:
        print(st, i)
        st = -1
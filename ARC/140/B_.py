n = int(input())
s = input()
ans = 0
cnt = 0
for i in range(1, n-1):
    if s[i] != 'R':continue
    a = i - 1
    c = i + 1
    while a >= 0 and s[a] == 'A':
        a -= 1
    while c < n and s[c] == 'C':
        c += 1
    val = min(i - a, c - i) - 1
    ans += val
    cnt += 1
print(min(ans, cnt*2))
n = int(input())
poem = set()
ans = 0
ind = 0
for i in range(n):
    s, t = map(str, input().split())
    if s not in poem and ans < int(t):
        ans = int(t)
        ind = i
    poem.add(s)
print(ind+1)
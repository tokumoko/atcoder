s = list(input())
for i in range(6):
    print(s[i % len(s)], end="")

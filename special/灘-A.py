n = int(input())
ans = n * (n-1) // 2
if n % 2 == 1:ans -= 1
print(ans)
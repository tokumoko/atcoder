from collections import defaultdict
dp=[defaultdict(list) for _ in range(3)]
dp[0][1]=3
a=dp[0][0]
print(a)
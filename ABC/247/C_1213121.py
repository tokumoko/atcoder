s = [[] for _ in range(16)]
s[0] = '1'
for i in range(1, 16):
    s[i] = [s[i-1] , str(i+1) , s[i-1]]
    s[i] = ' '.join(s[i])
n = int(input())
print(s[n-1])
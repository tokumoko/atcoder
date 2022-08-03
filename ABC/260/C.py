n, x, y = map(int, input().split())
red = [0] * n
blue = [0] * n
red[0] = 1
for i in range(n-1):
    blue[i] += red[i] * x
    red[i+1] += red[i] + blue[i]
    blue[i+1] += blue[i] * y
print(blue[n-1])
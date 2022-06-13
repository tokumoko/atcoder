x, a, d, n = map(int, input().split())
end = a + d*(n-1)
if x <= min(a, end) or x >= max(a, end):
    print(min(abs(x-a), abs(x-end)))
else:
    val = abs(x%d - a%d)
    print(min(val, abs(d) - val))
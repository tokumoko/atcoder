import sys
a = sys.getrecursionlimit()
def f(n):
    if n == 1000:return n
    else:return f(n+1)
print(f(3))
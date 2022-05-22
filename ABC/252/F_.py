import sys
sys.setrecursionlimit(1000000)
def f(x):
    if x > 10000:return x
    return f(x+1)
print(f(1))
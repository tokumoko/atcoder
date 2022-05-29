from math import gcd
n, a, b = map(int, input().split())
n_ans = n * (n+1) // 2
na = n // a
a_ans = na * (a + na*a) // 2
nb = n // b
b_ans = nb * (b + nb*b) // 2
ab = a * b // gcd(a, b)
nab = n // ab
ab_ans = nab * (ab + nab*ab) // 2
print(n_ans + ab_ans - a_ans - b_ans)
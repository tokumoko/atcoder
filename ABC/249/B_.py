S = list(input())
n = len(S)
m = len(set(S))
if not ''.join(S).islower() and n == m and n != 1 and not ''.join(S).isupper():
    print('Yes')
else:
    print('No')
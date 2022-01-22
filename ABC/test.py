N=312
s=list(str(N))
p=s.pop(0)
s.append(p)
N=int(''.join(s))
print(N)
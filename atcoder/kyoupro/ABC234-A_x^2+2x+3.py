def kansu(t):
    ft=t*t+2*t+3
    return ft

t=int(input())
print(kansu(kansu(kansu(t)+t)+kansu(kansu(t))))
S=list(input())
Smin=''.join(S)
Smax=''.join(S)
for i in range(len(S)-1):
    a=S[0]
    del(S[0])
    S.append(a)
    jS=''.join(S)
    if Smin>jS:Smin=jS
    if Smax<jS:Smax=jS
print(Smin)
print(Smax)
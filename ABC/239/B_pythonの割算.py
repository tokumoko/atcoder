x=list(input())
if len(x)==1:
    print(0)
elif x[0]=='-' and len(x)==2:
    print(-1)
elif x[0]!='-' or x[-1]=='0':
    del x[-1]
    print(''.join(x))
else:
    del x[-1]
    a=int(''.join(x[1:]))
    a=str(a+1)
    print('-'+a)
N=int(input())
for i in range(N):
    a=int(input())
    if i==0:
        s=a
    else:
        if s<a:
            print('up ' + str(a-s))
        elif s==a:
            print('stay')
        else :
            print('down ' + str(s-a))
        s=a
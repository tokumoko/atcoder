x1,y1,x2,y2=map(int,input().split())
if abs(x2-x1)==abs(y2-y1)==0:
    print('Yes')
elif abs(x2-x1)==abs(y2-y1)==1:
    print('Yes')
elif abs(x2-x1)==abs(y2-y1)==3:
    print('Yes')
elif abs(x2-x1)==1 and abs(y2-y1)==3:
    print('Yes')
elif abs(x2-x1)==3 and abs(y2-y1)==1:
    print('Yes')
elif abs(x2-x1)==2 and abs(y2-y1)==4:
    print('Yes')
elif abs(x2-x1)==4 and abs(y2-y1)==2:
    print('Yes')
elif abs(x2-x1)==0 and (abs(y2-y1)==4 or abs(y2-y1)==2):
    print('Yes')
elif (abs(x2-x1)==2 or abs(x2-x1)==4) and abs(y2-y1)==0:
    print('Yes')
else:
    print('No')
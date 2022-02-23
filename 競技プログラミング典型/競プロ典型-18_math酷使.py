import math
t=int(input())
l,x,y=map(int,input().split())
q=int(input())
for i in range(q):
    e=int(input())
    theta=e*360/t
    high=((1+math.cos(math.radians(theta+180)))/2)*l
    dist=math.sqrt(x**2+((y-(math.sin(math.radians(-theta))*(l/2)))**2))
    print(math.degrees(math.atan(high/dist)))
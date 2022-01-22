#できてないやつ
n=int(input())
i=1
s=0
while i*i<=n:
    s+=int(n/i-i+1)
    i+=1
print(s)
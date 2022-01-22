import bisect
ans=[]
a=[]
for shoko in range(1,10):
    for kousa in range(-9,9):
        for length in range(1,18):
            k=shoko+kousa*(length-1)
            if 0<=k and k<10:
                a=[]
                for i in range(length):
                    a.append(str(shoko+kousa*i))
                b=int(''.join(a))
                ans.append(b)
ans.sort()
X=int(input())
if X==10**17:
    print(111111111111111111)
    exit()
n=bisect.bisect_left(ans,X)
print(ans[n])
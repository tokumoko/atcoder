k = int(input())
h = 21
if k >= 60:
    k -= 60
    h += 1
k = str(k)
print(str(h) + ':' +  str(k.zfill(2)))
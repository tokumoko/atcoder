sr, sg, sb = map(str, input().split())
tr, tg, tb = map(str, input().split())
onaji = 0
if sr == tr:onaji += 1
if sg == tg:onaji += 1
if sb == tb:onaji += 1
if onaji == 1:
    print('No')
else:
    print('Yes')
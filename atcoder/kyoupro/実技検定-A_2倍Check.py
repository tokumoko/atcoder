n=input()
x=['1','2','3','4','5','6','7','8','9','0']
if len(n)==3 and n[0] in x and n[1] in x and n[2] in x:
    print(int(n)*2)
else: print('error')
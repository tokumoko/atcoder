s1=input()
s2=input()
if s1[0]=='.' and s1[1]=='#' and s2[0]=='#' and s2[1]=='.':
    print('No')
elif s1[0]=='#' and s1[1]=='.' and s2[0]=='.' and s2[1]=='#':
    print('No')
else : print('Yes')
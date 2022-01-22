L,R=map(int,input().split())
S=list(input())
list1=S[:L-1]
list2=S[::-1]
del list2[:len(S)-R]
if L!=1:del list2[-L+1:]
list3=S[R:]
ans=list1+list2+list3
for i in range(len(ans)):print(ans[i],end="")
print("")
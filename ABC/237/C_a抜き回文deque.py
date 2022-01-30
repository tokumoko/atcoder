from collections import deque
S=deque(list(input()))
while S[0]=='a':
    S.popleft()
    if len(S)==0:
        print('Yes')
        exit()
while S[-1]=='a':
    S.pop()
flag=True
l=len(S)-1
for i in range(len(S)//2):
    if S[i]!=S[l-i]:flag=False
print('Yes' if flag else 'No')
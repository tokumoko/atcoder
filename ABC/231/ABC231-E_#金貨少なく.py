N,X=map(int,input().split())
A=list(map(int,input().split()))
A.append(A[len(A)-1])
A.append(A[len(A)-1])
i=0
ans=0
while X!=0:
    if A[i]==A[i+1]:
        ans+=X/A[i]
        break
    money=X%A[i+1]
    if money!=0:
        if A[i+1]-money<money:
            X+=A[i+1]-money
            ans+=(A[i+1]-money)/A[i]
        elif A[i+1]-money==money:
            if (X%A[i+2])/A[i+1]>=A[i+1]/2:
                X+=A[i+1]-money
                ans+=(A[i+1]-money)/A[i]
            else:
                X-=money
                ans+=money/A[i]
        else : 
            X-=money
            ans+=money/A[i]
    i+=1
print(int(ans))
def find(a,n):
    s=0
    i=0
    while i<n-1:
        if a[i+1]>a[i]:
            s+=(a[i+1]-a[i]-1)
        elif a[i]>a[i+1]:
            s+=(a[i]-a[i+1]-1)
        else:
            s+=0
        i+=1
    return s





t=int(input())
i=0
while i<t:
    n=int(input())
    a=list(map(int,input().split()))
    print(find(a,n))
    i+=1
    

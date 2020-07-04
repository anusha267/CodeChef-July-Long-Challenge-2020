def rounds(n):
    chef=0
    morty=0
    i=0
    while i<n:
        x,y=map(str,input().split())
        a=findsum(x)
        b=findsum(y)
        if a>b:
            chef+=1
        elif b>a:
            morty+=1
        else:
            chef+=1
            morty+=1
        i+=1
    if chef>morty:
        print("0",chef)
    elif morty>chef:
        print("1",morty)
    else:
        print("2",chef)
    return 1

def findsum(a):
    s=0
    i=0
    while i<len(a):
        s=s+int(a[i])
        i+=1
    return s


t=int(input())
i=0
while i<t:
    n=int(input())
    score=rounds(n)
    i+=1

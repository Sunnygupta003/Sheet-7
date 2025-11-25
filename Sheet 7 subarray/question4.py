n=int(input( ))
a=list(map(int,input().split()))

for i in range(n):
    for j in range(i,n):
        s=(a[i:j+1])
        b=sum(s)
        print(s ,"->", b)
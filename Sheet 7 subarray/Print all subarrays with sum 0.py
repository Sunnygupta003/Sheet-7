b=int(input(" "))
a=list(map(int,input().split()))
n=len(a)
for i in range(n):
    s=0
    for j in range(i,n):
        s=s+a[j]
        if s==0:
            print(a[i:j+1])
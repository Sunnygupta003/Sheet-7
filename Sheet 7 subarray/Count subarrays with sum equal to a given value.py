b=int(input(" "))
a=list(map(int,input().split()))
k=2
count=0
n=len(a)
for i in range(n):
    s=0
    for j in range(i,n):
        s=s+a[j]
        if s==k:
            count=count+1
print(count)
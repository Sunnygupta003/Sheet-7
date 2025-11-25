a=[-2,1,-3,4,-1,2,1,-5,4]
n=len(a)
c=0
for i in range(n):
    for j in range(i,n):
        s=sum(a[i:j+1])
        if s>c:
            c=s
print(c)
a=[1,2,3,7,5]
b=12
n=len(a)
for i in range(n):
    s=0
    for j in range(i,n):
        s=s+a[j]
        if s == b :
            print(a[i:j+1])
a=[1,2,3]
n=len(a)
for i in range(n):
    for j in range(i,n):
        print(a[i:j+1])
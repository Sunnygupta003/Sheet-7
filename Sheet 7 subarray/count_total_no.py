a=[1,2,3]
n=len(a)
count=0
for i in range(n):
    for j in range(i,n):
        count=count+1
print(count)
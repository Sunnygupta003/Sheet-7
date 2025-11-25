n=int(input())
a=list(map(int,input().split()))
total=0
for i in range(n):
    for j in range(i,n):
        total=total+(sum(a[i:j+1]))
print(total)

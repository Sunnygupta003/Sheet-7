# b=int(input())
# a=list(map(int,input().split()))
# n=len(a)
# total=0
# maxi=float("-inf")
# for i in range(0,n):
#     total=total+a[i]
#     maxi=max(maxi,total)
#     if total<0:
#         total=0
# print(maxi)




# find the minimum subaary

b=int(input())
a=list(map(int,input().split()))

total=0
mini=float("inf")
for i in range(b):
    total=total+a[i]
    mini=min(mini,total)
    if total> 0:
        total=0
print(mini)
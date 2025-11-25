# a=[1,2,3]
# n=len(a)
# total=0
# for i in range (n):
#     for j in range (i,n):
#         total=total+sum(a[i:j+1])
# print(total)



a=[1,2,3]
n=len(a)
for i in range (n):
    for j in range (i,n):
        print(sum(a[i:j+1]))





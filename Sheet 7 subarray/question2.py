# n=int(input(" "))
# a=list(map(int,input("").split()))
# b=len(a)
# for i in range (b):
#     for j in range(i,b):
#         print(a[i:j+1])

n=int(input(" "))
a=list(map(int,input("").split()))

for i in range (len(a)):
    for j in range(i,len(a)):
        print(a[i:j+1])
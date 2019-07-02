n,a,d=map(int,input().split())
x=[]
x.append(a)
a1=a
for i in range(0,n-1):
    j=a1+d
    a1=j
    x.append(j)
sum=0
for i in x:
    sum=sum+i
print(sum)

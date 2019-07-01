s,e=map(int,input().split())
l=[]
for i in range(s+1,e):
    k=0
    for j in range(2,i):
        if(i%j==0):
            k+=1
    if(k<1):
        l.append(i)
for i in l:
    print(i,end=' ')

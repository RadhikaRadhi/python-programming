s,e=map(int,input().split())
l1=[]
for i in range(s+1,e):
    tot=0
    l2=[]
    i1=str(i)
    for j in i1:
        l2.append(int(j))
    for j in l2:
        tot=tot+(j**3)
    if(i==tot):
        l1.append(i)
for i in l1:
    print(i,end=' ')
        

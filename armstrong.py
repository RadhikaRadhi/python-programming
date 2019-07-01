num=int(input())
num1=str(num)
l1=[]
tot=0
for i in num1:
    l1.append(int(i))
for i in l1:
    tot=tot+(i**3)
if(num==tot):
    print("yes")
else:
    print("no")

  

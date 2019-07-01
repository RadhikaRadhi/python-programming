num=int(input())
k=0
for i in range(2,num):
  if(num%i==0):
    k+=1
if(k>0):
  print("yes")
else:
  print("no")

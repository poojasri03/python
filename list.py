n=int(input())
l=list(map(int,input()))[:n]
print(max(l))
print(min(l))
i,sum=0,0
for i in range(len(l)):
  sum=sum+l[i]
print(sum/n) 

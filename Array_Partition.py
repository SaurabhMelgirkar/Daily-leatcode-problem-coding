
# logic 1

l1=[1,4,3,2]
l1.sort()
l2=[]
n=len(l1)
for i in range(0,n,2):
    j=i+1
    l2.append([l1[i],l1[j]])
print(l2)
total=0
for pair in l2:
    total+=min(pair)
print(total)

# logic 2
l4=[1,4,3,2]
l4.sort()
totall=0
n=len(l4)
for x in range(0,n,2):
    totall+=l4[x]
print(totall)

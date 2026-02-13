# l1 = [2,4,3]
# l2 = [5,6,4]
# l3=[]
# l4=[]
# c=list(zip(l1,l2))
# for i,j in c:
#     l3.append(i+j)
# n=len(l3)
# for x in range(n):
#     if l3[x]>=10:
#         l4.append(l3[x]%10)
#     else:
#         l4.append(l3[x])

# print(l4)
        


# for i in l1:
#     for j in l2:
#         l3.append(i+j)
# print(l3)

# l1 = [2,4,3]
# l2 = [5,6,4]
l1=[9,7]
l2=[2,7]
l4 = []
carry = 0

for i, j in zip(l1, l2):
    total = i + j + carry

    l4.append(total % 10)   # digit
    carry = total // 10     # carry

# if carry is left after loop
if carry:
    l4.append(carry)

print(l4)

def one_sum():
    l=[1,2,3]   
    result=" "
    for i in l:
        result+=str(i)
    return result
res=one_sum()
sum=int(res)+1
l2=[]
l2.extend(str(sum))
l3=[]
for x in l2:
    l3.append(int(x))
print(l3)
    

# class Solution(object):
#     def plusOne(self, digits):
#         result = ""          
#         for i in digits:
#             result += str(i)

#         num = int(result) + 1
#         return list(map(int, str(num)))

# s=Solution()
# res=s.plusOne([9])
# print(res)


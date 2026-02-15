# # class Solution(object):
# #     def merge(self, nums1, m, nums2, n):
# #         pass
# def merge():
#     num1=[1,2,3,0,0,0,[]]
#     num2=[2,5,6]
#     n=[]
#     for i in num1 :
#         if  i!= 0 and i!=[]  :
#             n.append(i)
#     for j in num2 :
#         if  j!= 0 and j!=[]  :
#             n.append(j)
#     return n

# res=merge()
# print(res)        
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        temp = []
        
        # take only first m elements from nums1
        for i in range(m):
            temp.append(nums1[i])
        
        # take all elements from nums2
        for j in range(n):
            temp.append(nums2[j])
        
        temp.sort()
        
        # put sorted values back into nums1
        for k in range(m + n):
            nums1[k] = temp[k]


# Testing
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

s = Solution()
s.merge(nums1, m, nums2, n)

print(nums1)

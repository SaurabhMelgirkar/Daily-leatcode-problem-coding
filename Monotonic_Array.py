

# def is_mono(l):

#     for i in range(len(l)-1):
#         if l[i]> l[i+1]:
#             return False
#     return True

# res=is_mono([1,3,2])
# print(res)
class Solution(object):
    def isMonotonic(self, nums):
        inc = dec = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                inc = False
            if nums[i] < nums[i + 1]:
                dec = False

        return inc or dec


s = Solution()
res = s.isMonotonic([1, 3, 2])
print(res)




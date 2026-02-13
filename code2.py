class Solution(object):
    def removeDuplicates(self, nums):
        count=0
        new_nums=[]
        for no in nums:
            if no not in new_nums:
                new_nums.append(no)
                count+=1
        # nums=new_nums
        # nums[:len(new_nums)] = new_nums
        # print(new_nums)
        yield new_nums
        yield count

        # print(nums)
        # print(count)
        # return count 
    
        # return (new_nums , count)
obj=Solution()

# print(obj.removeDuplicates([1,1,2]))
re=obj.removeDuplicates([1,1,2])
print(next(re)) 
print(next(re))  
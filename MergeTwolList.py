class Solution(object):
    def mergeTwoLists(self,l1,l2):   
        # l1= list(input("enter list 1"))
        # l2=list(input("enter list 2"))
        list1=[]
        list1=l1 + l2
        list1.sort()
        return list1
obj1 = Solution()
print(obj1.mergeTwoLists([1,2,4],[1,3,4]))

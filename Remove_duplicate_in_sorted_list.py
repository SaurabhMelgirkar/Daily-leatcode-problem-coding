# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
                
        return head


# Helper function to convert list → linked list
def create_linked_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
        
    return head


# Helper function to print linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next


# Create linked list
head = create_linked_list([1,1,2,3,4])

# Call solution
s = Solution()
res = s.deleteDuplicates(head)

# Print result
print_linked_list(res)

class ListNode:
    def __init__(self,val=0, next=None):
        self.val=val
        self.next=next

class Solution :
    def remove_duplicate(self, head):
        current=head
        while current and current.next:
            if current.val==current.next.val:
                current.next=current.next.next
            else:
                current=current.next
        return head
    
    def create_LL (self,arr):
         if not arr:
             return None
         head=ListNode(arr[0])
         current =head
         for value in arr[1:]:
             current.next = ListNode(value)
             current = current.next
        
         return head
    def print_list(self,head):
        while head :
            print(head.val ,end=" ")
            head=head.next
s= Solution()
head=s.create_LL([1,1,2,3,4])
res=s.remove_duplicate(head)
s.print_list(res)


# # Call solution
# s = Solution()
# res = s.deleteDuplicates(head)

# # Print result
# print_linked_list(res)

             


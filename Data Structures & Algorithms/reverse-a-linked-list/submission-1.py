# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
       
        return self.helper(None, head)
    
    def helper(self, prev, curr):
        if not curr:
            return prev
        next = curr.next
        curr.next = prev
        prev = curr
        return self.helper(prev,next)
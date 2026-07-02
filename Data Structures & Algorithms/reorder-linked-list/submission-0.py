# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        middle = slow
        print(middle.val)
        while slow:
              next = slow.next
              slow.next = prev
              prev = slow 
              slow = next
        tail = prev
        left = head
        prevHead = None
        while left !=middle:
            if prevHead:
                prevHead.next = left
            next = left.next
            left.next = tail
            left =next
            prevHead = tail
            tail = tail.next
            
      
        
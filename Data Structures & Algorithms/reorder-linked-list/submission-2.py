# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
          slow = fast = head
          start = head
          mid = None
          prev = None
          while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
          
          mid = slow 
          end = slow.next
          mid.next = None
          while end:
              next = end.next
              end.next = prev 
              prev = end
              end = next
          end = prev
          while start != mid and end:
                next1 =start.next
                start.next = end
                start = next1
                
                next2 = end.next
                end.next = start
                end =next2 

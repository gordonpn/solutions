# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow_pointer = head
        fast_pointer = head
        
        while fast_pointer.next and fast_pointer.next.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        
        return False

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        stack = []
        
        current = head
        
        while current.next:
            stack.append(current)
            current = current.next
            
        head = current
        
        while stack:
            current.next = stack.pop()
            current = current.next
        
        current.next = None
            
        return head
​

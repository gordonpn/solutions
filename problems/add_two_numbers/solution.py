# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        result = ListNode()
        current_node = result
        
        while l1 is not None or l2 is not None:
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)
                
            sum_ = carry + l1.val + l2.val
            if carry > 0:
                carry -= 1
            if sum_ > 9:
                carry += 1
                sum_ -= 10
            
            current_node.next = ListNode(sum_)
            current_node = current_node.next
            
            l1 = l1.next
            l2 = l2.next
            
        if carry > 0:
            current_node.next = ListNode(carry)
                
        return result.next
                
            
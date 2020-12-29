# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        _list = []
        for node in lists:
            while node:
                _list.append(node.val)
                node = node.next
                
        _list = sorted(_list)
        
        head = pointer = ListNode()
        
        while _list:
            pointer.next = ListNode(_list.pop(0))
            pointer = pointer.next
            
        return head.next
                

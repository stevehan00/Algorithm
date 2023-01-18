# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        dq = collections.deque()
        
        if not head:
            return True
        
        node = head
        while node is not None:
            dq.append(node.val)
            node = node.next

        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        
        return True
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        l1_lst = []
        l2_lst = []
        
        if l1 is None and l2 is None:
            return None
        
        while l1:
            l1_lst.append(l1.val)
            l1 = l1.next
        while l2:
            l2_lst.append(l2.val)
            l2 = l2.next
        
        sums = l1_lst + l2_lst
        sums.sort()
        
        results: ListNode = ListNode(val=sums[0])
        node = results
        
        for i in range(1, len(sums)):
            node.next = ListNode(val=sums[i])
            node = node.next
        
        return results
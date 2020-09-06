# Definition for singly-linked list.
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        root = result = ListNode(None)
        hp = []
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(hp, (lists[i].val, i, lists[i]))
                
        while hp:
            node = heapq.heappop(hp)
            idx = node[1]
            result.next = node[2]
            
            result = result.next
            
            if result.next:
                heapq.heappush(hp, (result.next.val, idx, result.next))
        
        
        return root.next
            
        

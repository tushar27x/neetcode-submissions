# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode :
        dummy = ListNode(-1)
        temp = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            
            temp = temp.next
        
        
        temp.next = l1 if l1 else l2

        return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        res = lists[0]
        for i in range(1, len(lists)):
            res = self.merge(res, lists[i])
        
        return res
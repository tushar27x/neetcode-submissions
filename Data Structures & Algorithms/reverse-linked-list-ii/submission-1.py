# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        leftNode,rightNode = head, head
        dummy = ListNode(-1,head)
        dummyLeft, dummyRight = dummy, dummy
        i = 1
        while i < left:
            dummyLeft = dummyLeft.next
            leftNode = leftNode.next
            dummyRight = dummyRight.next
            rightNode = rightNode.next
            i += 1
        
        while i < right and rightNode != None and dummyRight != None:
            dummyRight = dummyRight.next
            rightNode = rightNode.next
            i+=1
        
        dummyRight = None if not rightNode else rightNode.next

        curr = leftNode
        prev = None
        while curr != dummyRight:
            nxt = curr.next
            curr.next = prev
            
            prev = curr
            curr = nxt
        
        dummyLeft.next = prev
        leftNode.next = dummyRight

        return dummy.next
        
        
        
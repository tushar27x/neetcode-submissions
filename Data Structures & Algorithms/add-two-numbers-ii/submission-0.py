# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self,head):
        curr = head
        prev, nxt = None, None
        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt
        
        return prev
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.rev(l1)
        l2 = self.rev(l2)

        carry = 0
        dummy = ListNode()
        curr = dummy
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v2 + v1 + carry
            val = s % 10
            carry = s // 10
            new_node = ListNode(val)
            curr.next = new_node
            curr = new_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        return self.rev(dummy.next)
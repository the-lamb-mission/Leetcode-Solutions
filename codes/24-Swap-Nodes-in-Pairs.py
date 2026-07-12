# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return None

        dummy = ListNode()
        tail = dummy

        while head != None:
            
            if head.next == None:
                tail.next = head
                break
            else:
                tail.next = ListNode(head.next.val)
                tail.next.next = ListNode(head.val)
                tail = tail.next.next
                head = head.next.next

        return dummy.next
            

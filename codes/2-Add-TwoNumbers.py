# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carrier = (l1.val + l2.val) // 10
        firstNode = ListNode((l1.val + l2.val) % 10)
        l1 = l1.next
        l2 = l2.next
        prevNode = firstNode

        while l1 != None and l2 != None:
            tempNode = ListNode((l1.val + l2.val + carrier) % 10)
            prevNode.next = tempNode
            carrier = (l1.val + l2.val + carrier) // 10
            prevNode = tempNode
            l1 = l1.next
            l2 = l2.next
        
        #when l1 is longer than l2
        while l1 != None:
            tempNode = ListNode((l1.val + carrier) % 10)
            prevNode.next = tempNode
            carrier = (l1.val + carrier) // 10
            prevNode = tempNode
            l1 = l1.next

        #when l2 is longer than l1
        while l2 != None:
            tempNode = ListNode((l2.val + carrier) % 10)
            prevNode.next = tempNode
            carrier = (l2.val + carrier) // 10
            prevNode = tempNode
            l2 = l2.next

        #carrier still remain after addition
        if carrier > 0:
            prevNode.next = ListNode(carrier)

        return firstNode


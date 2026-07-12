# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None

        dummy = ListNode()
        tail = dummy
        flag = False


        while head != None:
            
            temp = head
            for i in range(k):
                if temp == None:
                    flag = True
                    break
                else:
                    temp = temp.next

            if flag:
                tail.next = head
                break
            else:
                temp = []
                for i in range(k):
                    temp.append(head.val)
                    head = head.next
                for i in range(k):
                    tail.next = ListNode(temp.pop())
                    tail = tail.next
        return dummy.next

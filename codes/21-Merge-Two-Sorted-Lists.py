# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None and list2 == None:
            return None
        
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            if list1.val < list2.val:
                head = ListNode(list1.val, None)
                list1 = list1.next
            else:
                head = ListNode(list2.val, None)
                list2 = list2.next
        
        cur = head
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp = ListNode(list1.val, None)
                cur.next = temp
                cur = temp
                list1 = list1.next
            else:
                temp = ListNode(list2.val, None)
                cur.next = temp
                cur = temp
                list2 = list2.next

        if list1 == None:
            cur.next = list2
        elif list2 == None:
            cur.next = list1

        return head


        

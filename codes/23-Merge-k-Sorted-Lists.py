# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Idea: Similar to merge sort, slice lists of linkedlists to half until single sorted linkedlist, then sort two. use recursion to reduce time.
        def recur(a):
            p = len(a)
            if p <= 1:
                return a[0]
            else:
                m = recur(a[:p//2])
                n = recur(a[p//2:])

                dummy = ListNode()
                tail = dummy
                
                while m and n:
                    if m.val < n.val:
                        tail.next = m
                        m = m.next 
                    else:
                        tail.next = n
                        n = n.next
                    tail = tail.next
                if m:
                    tail.next = m
                if n:
                    tail.next = n
                
                return dummy.next
        
        if lists == []:
            return None
        return recur(lists)

                



                

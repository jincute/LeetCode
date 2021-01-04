# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def dc(lists):
            if len(lists) == 1:
                return lists[0]
            mid = len(lists) // 2
            L = dc(lists[:mid])
            R = dc(lists[mid:])
            return merge(L, R)

        def merge(l, r):
            cur = ListNode(0)
            k = cur

            while l and r:
                if l.val < r.val:
                    k.next = ListNode(l.val)
                    l = l.next
                else:
                    k.next = ListNode(r.val)
                    r = r.next

                k = k.next

            k.next = l or r
            temp = cur.next
            cur.next = None

            return temp

        return dc(lists) if lists else None

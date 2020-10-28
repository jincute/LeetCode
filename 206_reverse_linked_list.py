# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #iteratively
        '''
        prev = None
        curr = head
        while curr != None:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev
        '''

        #recursively
        if head == None:
            return None

        return reverse(head, None)

def reverse(head, newhead):
    if head == None:
        return newhead
    nextnode = head.next
    head.next = newhead
    newhead = head
    head = nextnode

    return reverse(head, newhead)

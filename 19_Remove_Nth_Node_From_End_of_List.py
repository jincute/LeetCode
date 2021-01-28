# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head
        post = head
        for i in range(n - 1):
            curr = curr.next
        while curr.next != None:
            temp = post
            post = post.next
            curr = curr.next
        if post == head:
            head = head.next
        else:
            temp.next = post.next
        return head

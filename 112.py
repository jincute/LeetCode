import pdb
from collections import Counter

#Given a sorted linked list, delete all duplicates such that each element appear only once.
'''
Example 1:
	Input:  null
	Output: null


Example 2:
	Input:  1->1->2->null
	Output: 1->2->null

Example 3:
	Input:  1->1->2->3->3->null
	Output: 1->2->3->null
'''

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution(object):
    """
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        # write your code here
        if head == None:
            return None
        p = head
        while p.next != None:
            if p.val != p.next.val:
                p = p.next
            else:
                p.next = p.next.next
        return head

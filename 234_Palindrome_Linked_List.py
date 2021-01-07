# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # stack solution
        stack = []
        p = head
        while p:
            stack.append(p.val)
            p = p.next

        # [::-1] 顺序相反
        return stack == stack[::-1]

        '''

        # 空间为 O(1) 的实现
        if head is None or head.next is None:
            return True

        # 快慢指针找到链表中点。链表长度为3，则中点为2；链表长度为4，中点也为2
        slow = fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # 对链表中点之后的链表进行翻转，使用自定义 reverse 函数
        mid = slow.next
        mid = self.reverse(mid)

        # 依次比较链表中点前与链表中点后的元素值，如果出现不等则返回 False
        while mid:
            if head.val != mid.val:
                return False
            head = head.next
            mid = mid.next
        return True

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            cur.next, cur, pre = pre, cur.next, cur
        return pre
    '''


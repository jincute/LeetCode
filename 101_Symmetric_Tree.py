# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 递归解法
        '''
        # 原树 tree; 镜像树 mirror_tree
        # tree.left.val == mirror_tree.right.val and tree.right.val == mirror_tree.left.val
        # 空树也是对称
        if root == None:
            return True
        return self.mirror_tree(root.left, root.right)

    def mirror_tree(self,left, right):
        if left == None or right == None:
            if left == None and right == None:
                return True
            else:
                return False
        return left.val == right.val and self.mirror_tree(left.left, right.right) and self.mirror_tree(left.right, right.left)
        '''

        # 迭代思路：用 python 的 deque 双向队列
        if root == None:
            return True
        deq = deque([root.left, root.right])
        while deq:
            root_right = deq.pop()
            root_left = deq.pop()
            if root_left == None and root_right == None:
                continue
            if root_left == None or root_right == None:
                return False
            if root_left.val != root_right.val:
                return False
            deq.extend([root_left.left, root_right.right, root_left.right, root_right.left])
        return True


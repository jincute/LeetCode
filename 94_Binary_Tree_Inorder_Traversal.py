# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # iteration solution
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result

    '''
    # recursive solution

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.inorder(root, result)
        return result

    def inorder(self, node, r):
        if node == None:
            return None
        else:
            self.inorder(node.left,r)
            r.append(node.val)
            self.inorder(node.right,r)
        return r
    '''

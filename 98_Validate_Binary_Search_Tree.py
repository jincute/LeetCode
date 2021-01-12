# Definition for a binary tree node.
import pdb

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.valid(root, float('-inf'), float('inf'))
     
    def valid(self, root, min, max):
        #print('begin root,min,max: ', root.val, min, max)
        if root is None:
            print('empty')
        else:
            print('begin root,min,max: ', root.val, min, max)
        pdb.set_trace()
        if root is None:
            return True
        if root.val <= min or root.val >= max:
            return False 
        print('root,min,max: ', root.val, min, max)
        return self.valid(root.left, min, root.val) and self.valid(root.right, root.val, max)


node5 =  TreeNode(5)
node1 = TreeNode(1)
node4 = TreeNode(6)
node3 = TreeNode(3)
node6 = TreeNode(7)

node5.left = node1
node5.right = node4
node4.left = node3
node4.right = node6

print(Solution().isValidBST(node5))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 递归法，关键在于设置好边界 recursive
        # 对于left子树，左节点需要确定上界，右节点需要确定上界和下界
        # 对于right子树，左节点需要确定上界和下界，右节点需要确定下界
        '''
        def compute_BST(root, max_=float('inf'),min_=float('-inf')):
            if not root:
                return True
            cur = root.val
            if cur >= max_ or cur <= min_:
                return False
            if not compute_BST(root.left,cur,min_):
                return False
            if not compute_BST(root.right,max_,cur):
                return False
            return True
        return compute_BST(root)
        '''

        # 迭代法 iteration
        # dfs 或者 bfs，用dfs，pop(0)
        # 会牺牲空间获取时间
        # 主要是创建一个可迭代的对象，例如列表，队列，预存一组数据，每次循环判断序列是否为空，不为空则判断条件，添加数据进去，知道队列为空。迭代算法也需要依赖前面的值求后面的值，像max_和min_的动态变化
        if not root:
            return True
        result = [(root, float('inf'), float('-inf'))]
        while result:
            # 每次处理一个节点
            root, max_, min_ = result.pop()
            if not root:
                continue
            val = root.val
            if val >= max_ or val <= min_:
                return False
            result.append((root.left, val, min_))
            result.append((root.right, max_, val))
        # 如果都满足，则 result 为空，返回 True
        return True

        # 中序遍历：左-中-右，按照从小到大的顺序排列，所以中序遍历将值存入列表之后判断是否是从小到大的顺序排列
        if not root:
            return True
        result = []

        def mid_traversal(root):
            if root.left:
                mid_traversal(root.left)
            result.append(root.val)
            if root.right:
                mid_traversal(root.right)

        mid_traversal(root)

        if result == sorted(result):
            return True
        else:
            return False
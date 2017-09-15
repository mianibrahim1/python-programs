# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None and t2 == None:
            return None
        elif t1 == None:
            t3.val = TreeNode(t2.val)
        elif t2 == None:
            t3.val = TreeNode(t1.val)
        else:
            t3.val = TreeNode(t1.val + t2.val)
        t3.left = self.mergeTrees(t1.left,t2.left)
        t3.right = self.mergeTrees(t2.right,t2.right)
        return t3

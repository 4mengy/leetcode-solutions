# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def findroot(inorder, preorder):
            if not preorder:
                return None
            
            if len(preorder) == 1:
                return TreeNode(preorder[0])
            
            root_v = preorder[0]
            root = TreeNode(root_v)
            root_i = inorder.index(root_v)
            root.left = findroot(inorder[:root_i], preorder[1:root_i + 1])
            root.right = findroot(inorder[root_i + 1:], preorder[root_i + 1:])
            
            return root
            
        return findroot(inorder, preorder)
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        def findroot(inorder, postorder):
            if not postorder:
                return None
            
            if len(postorder) == 1:
                return TreeNode(postorder[0])
            
            root_v = postorder[-1]
            root = TreeNode(root_v)
            root_i = inorder.index(root_v)
            root.left = findroot(inorder[:root_i], postorder[:root_i])
            root.right = findroot(inorder[root_i + 1:], postorder[root_i: -1])
            
            return root
            
        return findroot(inorder, postorder)
            
        
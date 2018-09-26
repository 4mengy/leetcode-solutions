# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        oroot = root
        pre = None
        while root:
            if key == root.val:
                break
            elif key < root.val:
                pre = root
                root = root.left
            else:
                pre = root
                root = root.right
        
        if not root:
            return oroot
        
        if not root.left and not root.right:
            if not pre:
                return None
            elif pre.left == root:
                pre.left = None
            else:
                pre.right = None
        elif root.left and not root.right:
            root.val = root.left.val
            root.right = root.left.right
            root.left = root.left.left
        elif root.right and not root.left:
            root.val = root.right.val
            root.left = root.right.left
            root.right = root.right.right
        else:
            spre = root
            successor = root.right
            while True:
                if successor.left:
                    spre = successor
                    successor = successor.left
                    continue
                else:
                    break
            
            root.val = successor.val
            if spre.left == successor:
                spre.left = successor.right
            else:
                spre.right = successor.right
        
        return oroot
        
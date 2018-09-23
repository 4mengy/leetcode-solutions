# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        s = [root]
        visited = set()
        ret = []
        
        while len(s):
            curr = s[-1]
            if curr.left and curr.left not in visited:
                s.append(curr.left)
            elif curr not in visited:
                ret.append(curr.val)
                visited.add(curr)
                s.pop()
            
                if curr.right and curr.right not in visited:
                    s.append(curr.right)
                
        return ret

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.deque = deque()
        
        self.deque.append(root)
        while True:
            curr = self.deque[0]
            if curr.left:
                self.deque.append(curr.left)
                if curr.right:
                    self.deque.append(curr.right)
                    self.deque.popleft()
                else:
                    break
            else:
                break
            

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        parent = self.deque[0]
        if parent.left:
            parent.right = TreeNode(v)
            self.deque.append(parent.right)
            self.deque.popleft()
            return parent.val
        else:
            parent.left = TreeNode(v)
            self.deque.append(parent.left)
            return parent.val
        
        

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.has = False
        self.visited = set()
        if root:
            self.stack.append(root)
            self.has = True
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.has
        

    def next(self):
        """
        :rtype: int
        """
        while self.stack:
            curr = self.stack[-1]
            if curr.left and curr.left not in self.visited:
                self.stack.append(curr.left)
            elif curr not in self.visited:
                self.visited.add(curr)
                self.stack.pop()
            
                if curr.right and curr.right not in self.visited:
                    self.stack.append(curr.right)
                
                if not self.stack:
                    self.has = False
                return curr.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
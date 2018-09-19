# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from Queue import Queue

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return 
        
        q = Queue()
        q.put(root)
        
        while q.qsize():
            s = q.qsize()
            pre = q.get()
            if pre.left:
                q.put(pre.left)
            if pre.right:
                q.put(pre.right)
            for _ in range(s - 1):
                item = q.get()
                pre.next = item
                pre = item
                if pre.left:
                    q.put(pre.left)
                if pre.right:
                    q.put(pre.right)
            pre.next = None
            
        
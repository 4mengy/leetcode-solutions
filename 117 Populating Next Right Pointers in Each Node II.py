# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root:
            item = root
            while item:
                if item.left and item.right:
                    item.left.next = item.right
                    target = item.right
                elif not item.left and item.right:
                    target = item.right
                elif item.left and not item.right:
                    target = item.left
                else:
                    item = item.next
                    continue
                item = item.next
                while item:
                    if item.left: break
                    if item.right: break
                    item = item.next
                
                if not item:
                    target.next = None
                elif item.left:
                    target.next = item.left
                else:
                    target.next = item.right
            while root:
                if root.left:
                    root = root.left
                    break
                if root.right: 
                    root = root.right
                    break
                root = root.next
            
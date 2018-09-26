class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.cnt = 1
        self.left = None
        self.right = None


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.bst = None
        for x in nums:
            self.add_v(x)
            
            
    def add_v(self, val):
        if not self.bst:
            self.bst = TreeNode(val)
            return
        
        curr = self.bst
        while True:
            if curr.val == val:
                curr.cnt += 1
                break
            elif val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    break
            elif val > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    break
            

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.add_v(val)
        cnt = 0
        s = [self.bst]
        v = set()
        while s:
            curr = s[-1]
            if curr.right and curr.right not in v:
                s.append(curr.right)
                continue
            elif curr not in v:
                cnt += curr.cnt
                s.pop()
                v.add(curr)
                if cnt >= self.k:
                    return curr.val
                
                if curr.left:
                    s.append(curr.left)
                    continue
                

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
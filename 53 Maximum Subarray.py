import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = -sys.maxint - 1
        sa = -sys.maxint - 1
        sb = -sys.maxint - 1
        
        for n in nums:
            sb = max(n, sa + n)
            m = max(sb, m)
            sa = sb
            
        return m
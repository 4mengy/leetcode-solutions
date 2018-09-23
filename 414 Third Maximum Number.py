class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = [None, None, None]
        for i in nums:
            if i in m:
                continue
                
            if i > m[1] and i < m[2]:
                m[0] = m[1]
                m[1] = i
            elif i > m[2]:
                m[0] = m[1]
                m[1] = m[2]
                m[2] = i
            elif i > m[0] and i < m[1]:
                m[0] = i
            
        if m[0] is not None and m[1] is not None and m[2] is not None:
            return m[0]
        else:
            return m[2]
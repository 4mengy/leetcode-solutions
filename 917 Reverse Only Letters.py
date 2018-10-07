class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        lpos = 0
        rpos = len(S) - 1
        
        ret = []
        while lpos < len(S):
            if S[lpos].isalpha():
                while not S[rpos].isalpha():
                    rpos -= 1
                ret.append(S[rpos])
                rpos -= 1
            else:
                ret.append(S[lpos])
            lpos += 1
        return ''.join(ret)
                
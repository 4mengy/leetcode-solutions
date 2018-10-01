class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for w in word:
            node = node.setdefault(w, {})
        node['#'] = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def _s(root, word):
            if not isinstance(root, dict) or not root:
                return False
            for i, w in enumerate(word):
                if w == '.':
                    return reduce(lambda x, y: x or y, [_s(m, word[i+1:]) for m in root.itervalues()])
                root = root.get(w, None)
                if not root:
                    return False
            if root.get('#', False):
                return True
            return False
        
        return _s(self.root, word)
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
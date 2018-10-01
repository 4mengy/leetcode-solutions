class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        class TrieTree(object):
            def __init__(self):
                self.root = {}
                
            def insert(self, word):
                node = self.root
                for w in word:
                    node = node.setdefault(w, {})
                node['#_word'] = True
                
            def search(self, word):
                node = self.root
                for i, w in enumerate(word):
                    node = node.get(w, None)
                    if not node:
                        return word
                    if node.get('#_word', False):
                        return word[:i + 1]
                return word
                    
        tire = TrieTree()
        for item in dict:
            tire.insert(item)
            
        ret = []
        for w in sentence.split(' '):
            ret.append(tire.search(w))
        
        return ' '.join(ret)
            
        
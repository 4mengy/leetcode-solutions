class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        node = self.root
        for w in key:
            node = node.setdefault(w, {})
        node['#_val'] = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for w in prefix:
            node = node.get(w, None)
            if not node:
                return 0
        
        def s(node):
            if not node or not isinstance(node, dict):
                return 0
            return node.get('#_val', 0) + reduce(lambda x, y: x + y, [s(i) for i in node.itervalues()])
            
        return s(node)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# Implement a trie with insert, search, and startsWith methods.

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None] * 26 # addressed with integer
    
    @staticmethod
    def index(char):
        return ord(char) - ord('a')
    
    def has_no_key(self, char):
        return self.children[self.index(char)] is None

    def put(self, char):
        self.children[self.index(char)] = TrieNode()
    
    def get(self, char):
        return self.children[self.index(char)]
            

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if node.has_no_key(c):
                node.put(c)
            node = node.get(c)
        node.is_end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if node.has_no_key(c):
                return False
            node = node.get(c)
        return node.is_end        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if node.has_no_key(c):
                return False
            node = node.get(c)
        return True    


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


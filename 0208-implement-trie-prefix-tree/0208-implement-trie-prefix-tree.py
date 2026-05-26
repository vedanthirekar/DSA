class Trie:

    def __init__(self):
        self.node = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.node
        for w in word:
            if w not in curr.children:
                curr.children[w] = TreeNode()
            curr = curr.children[w]
            
        curr.wordends = True

    def search(self, word: str) -> bool:
        curr = self.node
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return curr.wordends

    def startsWith(self, prefix: str) -> bool:
        curr = self.node
        for w in prefix:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return True
        

class TreeNode:
    def __init__(self):
        self.children = {}
        self.wordends = False



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
class WordDictionary:

    def __init__(self):
        self.node = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.node
        for w in word:
            if w not in curr.children:
                curr.children[w] = TreeNode()
            curr = curr.children[w]
        curr.endofword = True

    def search(self, word: str) -> bool:
        curr = self.node
        def dfs(i, curr):
            if i == len(word):
                return curr.endofword

            if word[i] in curr.children:
                return dfs(i+1, curr.children[word[i]])

            if word[i] == ".":
                for child in curr.children.values():
                    if dfs(i+1, child):
                        return True
                return False
            
            # dfs(i+1)
            return False

        return dfs(0, curr)


class TreeNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

from _collections import defaultdict
class WordNode:
    def __init__(self):
        self.children = defaultdict(WordNode)
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = WordNode()

    def insert(self, word):
        node = self.root
        for i in word:
            node = node.children[i]
        node.isEnd = True

    def search(self, word):
        return self.DFS(word, 0, self.root, False)

    def startsWith(self, word):
        return self.DFS(word, 0, self.root, True)

    def DFS(self, word, idx, node, searchPrefix):
        if idx == len(word):
            if searchPrefix:
                return True
            elif node.isEnd:
                return True
            else:
                return False

        if word[idx] in node.children:
            return self.DFS(word, idx+1, node.children[word[idx]], searchPrefix)
        else:
            return False

if __name__ == '__main__':
    T = Trie()
    T.insert('aka')
    ans = T.search('aka')
    print(ans)
    isPrefix = T.startsWith('a')

    a = 1
    print(a >> 1)
    print(format(12, 'b'))
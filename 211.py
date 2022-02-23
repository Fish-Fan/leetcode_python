from _collections import defaultdict


# class WordNode:
#     def __init__(self):
#         self.children = {}
#         self.isEnd = False
#
# class WordDict:
#     def __init__(self):
#         self.root = WordNode()
#
#     def addWord(self, word):
#         node = self.root
#         for i in word:
#             if i not in node.children:
#                 node.children[i] = WordNode()
#                 node = node.children[i]
#             else:
#                 node = node.children.get(i)
#         node.isEnd = True
#
#     def searchWord(self, word):
#         stack = [(self.root, word)]
#         while stack:
#             node, w = stack.pop()
#             if not w:
#                 if node.isEnd:
#                     return True
#             elif w[0] == '.':
#                 for i in node.children:
#                     stack.append((i, w[1:]))
#             elif w[0] in node.children:
#                 n = node.children.get(w[0])
#                 stack.append((n, w[1:]))
#         return False

class WordNode:
    def __init__(self):
        self.children = defaultdict(WordNode)
        self.isEnd = False

class WordDict:
    def __init__(self):
        self.root = WordNode()

    def addWord(self, word):
        node = self.root
        for i in word:
            node = node.children[i]
        node.isEnd = True

    def searchWord(self, word):
        node = self.root
        return self.DFS(node, word)

    def DFS(self, node, word):
        if not word and node.isEnd:
            return True
        elif word[0] == '.':
            for i in node.children.values():
                res = self.DFS(i, word[1:])
                if res:
                    return True
        elif word[0] in node.children:
            return self.DFS(node.children.get(word[0]), word[1:])
        return False

if __name__ == '__main__':
    mydict = WordDict()
    mydict.addWord('aka')
    mydict.addWord('akaend')
    mydict.addWord('bka')

    ans = mydict.searchWord('.ka')
    print(ans)
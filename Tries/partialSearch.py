    #/usr/bin/python2 
    # Trie class
    class TrieNode:
        def __init__(self):
            self.root = dict()
            self.count=0

        def insert(self, word):
            current = self.root
            for letter in word:
                current = current.setdefault(letter, {})
            current.setdefault('_END')

        def search(self, word):
            current = self.root
            for letter in word:
                if letter not in current:
                    return False
                current = current[letter]
                if "_END" in current:
                    return True
            return False

        def startsWith(self, word):
            current = self.root
            for letter in word:
                if letter not in current:
                    return False
                current = current[letter]
            return current

    def traverse(current, count):
        if not current:
                return 0
        if '_END' in current:
            count += 1
        for k in current.keys():
            if k != '_END':
                count += traverse(current[k], 0)
        return count

    # test
    def test():
        trie = TrieNode()
        n = int(raw_input())
        while n > 0:
            op, contact = raw_input().split()
            if op == "add":
                trie.insert(contact)
            elif op == "find":
                current = trie.startsWith(contact)
                print traverse(current, 0)
            n -= 1

    test()

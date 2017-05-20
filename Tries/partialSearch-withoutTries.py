prefixIndex = {}

def tokenize(contact):
    return [contact[0:x] for x in xrange(1, len(contact)+1)]

def insert(contact):
    for token in tokenize(contact):
        prefixIndex[token] = prefixIndex.get(token,0)+1
def find(contact):
    return prefixIndex.get(contact,0)
def test():
    n = int(raw_input())
    while n > 0:
        op, contact = raw_input().split()
        if op == "add":
            insert(contact)
        elif op == "find":
             print find(contact)
        n -= 1

test()
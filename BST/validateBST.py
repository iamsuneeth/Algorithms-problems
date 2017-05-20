''' validate a BST tree if a node is passed 
Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

import sys
def check(root,minim,maxim):
    if not root:
        return True
    if root.data<=minim or root.data>=maxim:
        return False
    return check(root.left,minim,root.data) and check(root.right,root.data,maxim)
    
def check_binary_search_tree_(root):
    return check(root,-sys.maxint,sys.maxint)
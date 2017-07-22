"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def check_cycle(data,node):
    if node is None:
        return False
    if node.data in data:
        return True
    data.append(node.data)
    return check_cycle(data,node.next)


def has_cycle(head):
    if head is None:
        return False
    dataList = []
    dataList.append(head.data)
    return check_cycle(dataList,head.next)
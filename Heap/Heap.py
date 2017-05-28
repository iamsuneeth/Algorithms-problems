class Heap(object):
    def __init__(self, comparator):
        self.compare = comparator
        self.heap = []
        self.heapSize = 0
    
    def getHeapSize(self):
        return self.heapSize
        
    def getLeftIndex(self, index):
        return 2*index+1
    
    def getRightIndex(self, index):
        return 2*index+2

    def getParentIndex(self, index):
        return (index-1)/2

    def getLeftChild(self, parentIndex):
        return self.heap[self.getLeftIndex(parentIndex)]

    def getRightChild(self, parentIndex):
        return self.heap[self.getRightIndex(parentIndex)]
    
    def getParent(self, index):
        return self.heap[self.getParentIndex(index)]
    
    def hasParent(self, index):
        return self.getParentIndex(index) >=0

    def hasLeftChild(self, index):
        return self.getLeftIndex(index) < self.heapSize
    
    def hasRightChild(self, index):
        return self.getRightIndex(index) < self.heapSize

    def add(self, elem):
        self.heap.append(elem)
        self.heapSize+=1
        self.heapifyUp()
    
    def remove(self):
        elem = self.heap[0]
        self.heap[0] = self.heap[self.heapSize-1]
        self.heap.pop(self.heapSize-1)
        self.heapSize -= 1
        self.heapifyDown()
        return elem
    
    def peek(self):
        if self.heapSize ==0:
            raise Exception
        else:
            return self.heap[0]    

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            optimumindex = self.getLeftIndex(index)
            if self.hasRightChild(index) and self.compare(self.getLeftChild(index), self.getRightChild(index)):
                optimumindex = self.getRightIndex(index)
            if not self.compare(self.heap[index],self.heap[optimumindex]):
                break
            else:
                self.swap(index, optimumindex)
            index = optimumindex
    
    def heapifyUp(self):
        index = self.heapSize - 1
        while self.hasParent(index) and self.compare(self.getParent(index),self.heap[index]):
            self.swap(self.getParentIndex(index),index)
            index = self.getParentIndex(index)
    
    def swap(self,indexOne, IndexTwo):
        self.heap[indexOne], self.heap[IndexTwo] = self.heap[IndexTwo], self.heap[indexOne]

            

class MaxHeap(Heap):
    def __init__(self):
        super(MaxHeap, self).__init__(self.comparator)

    def comparator(self,a,b):
        return a<b

class MinHeap(Heap):
    def __init__(self):
        super(MinHeap, self).__init__(self.comparator)

    def comparator(self,a,b):
        return a>b
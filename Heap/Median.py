from Heap import MinHeap,MaxHeap

def compare(a,b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
def avg(a,b):
    return (a + b)/2.0
def fetchMedian(median,elem, left, right):
    result = compare(left.getHeapSize(), right.getHeapSize())
    if result == 1 :
        if elem < median:
            right.add(left.remove())
            left.add(elem)
        else:
            right.add(elem)
        median = avg(left.peek(),right.peek())
    elif result == 0 :
        if elem < median:
            left.add(elem)
            median = left.peek()
        else:
            right.add(elem)
            median = right.peek()
    else:
        if elem < median:
            left.add(elem)
        else:
            left.add(right.remove())
            right.add(elem)
        median = avg(left.peek(),right.peek())
    print left.heap
    print right.heap
    return float(median)




leftHeap = MaxHeap()
rightHeap = MinHeap()
n = int(raw_input().strip())
a_i = 0
median = 0
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    median = fetchMedian(median,a_t,leftHeap,rightHeap)
    print median
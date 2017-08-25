
def merge(arr,start,middle,end):
    leftStart = start
    leftEnd = middle
    rightStart = middle + 1
    rightEnd = end
    result=[]
    count=0
    
    while leftStart <= leftEnd and rightStart <= rightEnd:
        if arr[leftStart]<=arr[rightStart]:
            result.append(arr[leftStart])
            leftStart+=1
        else:
            count+=(leftEnd-leftStart+1)
            result.append(arr[rightStart])
            rightStart+=1
    while leftStart<= leftEnd:
        result.append(arr[leftStart])
        leftStart+=1
    while rightStart<= rightEnd:
        result.append(arr[rightStart])
        rightStart+=1
    for i in range(len(result)):
        arr[start+i] = result[i]
    
  
    return count

    

def mergeSort(arr,start,end):
    count=0
    if start<end:
        middle = (start + end)//2
        count=mergeSort(arr,start,middle)
        count+=mergeSort(arr,middle+1,end)
        count+=merge(arr,start,middle,end)
    return count


def main():
    arr = [2,1,3,1,2]
    result = [-1 for x in arr]
    count = mergeSort(arr,0, len(arr) - 1)
    print(arr,count)


main()

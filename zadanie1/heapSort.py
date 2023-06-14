def maxHeapify(A, i, size):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if(left < size and A[left] > A[largest]):
        largest = left
   
    if(right < size and A[right] > A[largest]):
        largest = right
    
    if(largest != i):
        A[largest], A[i] = A[i], A[largest]
        maxHeapify(A, largest ,size-1)

def heapSort(A, size):
    for i in range((size // 2) - 1, -1, -1):
        maxHeapify(A, i, size)

    for i in range(size - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        maxHeapify(A, 0, i)
    return A
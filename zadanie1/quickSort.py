def partition(A, first, last):
    pivot = A[last]
    smaller = first
    for j in range(first, last):
        if A[j] <= pivot:
            A[smaller], A[j] = A[j], A[smaller]
            smaller = smaller + 1
    A[smaller], A[last] = A[last], A[smaller]
    return smaller

def quickSort(A, p, r):
    if p < r :
        q = partition(A, p, r - 1)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)
    return A    

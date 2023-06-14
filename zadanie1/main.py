from quickSort import quickSort;
from heapSort import heapSort;
from mergeSort import mergeSort;

data = [1, 7, 4, 1, 10, 9, -2]
size = len(data)

print(quickSort(data.copy(), 0, size))
print(heapSort(data.copy(), size ))
print(mergeSort(data.copy()))
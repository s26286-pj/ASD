from quickSort import quickSort;
from heapSort import heapSort;
from mergeSort import mergeSort;

import random
import time

def measureExecutionTime(callback, data):
    startTime = time.time()
    callback(data)
    endTime = time.time()
    return endTime - startTime

def generateRandomArray(size, startRange, endRange):
    randomArray = [random.randint(startRange, endRange) for _ in range(size)]
    return randomArray

data = generateRandomArray(300000, -10000, 10000)
sortedData = quickSort(data.copy())

reversedData = sortedData.copy()
reversedData.reverse()

# print("data", data)
# print("sortedData", sortedData)
# print("reversedData", reversedData)

print("Quicksort:", measureExecutionTime(quickSort, data.copy()), "seconds");
print("HeapSort:", measureExecutionTime(heapSort, data.copy()), "seconds");
print("MergeSort:", measureExecutionTime(mergeSort, data.copy()), "seconds");

# print("Quicksort:", measureExecutionTime(quickSort, sortedData.copy()), "seconds");
print("HeapSort:", measureExecutionTime(heapSort, sortedData.copy()), "seconds");
print("MergeSort:", measureExecutionTime(mergeSort, sortedData.copy()), "seconds");

# print("Quicksort:", measureExecutionTime(quickSort, reversedData.copy()), "seconds");
print("HeapSort:", measureExecutionTime(heapSort, reversedData.copy()), "seconds");
print("MergeSort:", measureExecutionTime(mergeSort, reversedData.copy()), "seconds");


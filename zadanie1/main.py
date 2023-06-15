from quickSort import quickSort;
from heapSort import heapSort;
from mergeSort import mergeSort;

import random
import time

def measureExecutionTime(callback):
    startTime = time.time()
    callback(data.copy())
    endTime = time.time()
    return endTime - startTime

def generateRandomArray(size, startRange, endRange):
    randomArray = [random.randint(startRange, endRange) for _ in range(size)]
    return randomArray

data = generateRandomArray(300000, -10000, 10000)
print("Quicksort:", measureExecutionTime(quickSort), "seconds");
print("HeapSort:", measureExecutionTime(heapSort), "seconds");
print("MergeSort:", measureExecutionTime(mergeSort), "seconds");


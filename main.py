import os
import time
import random
import sys
from memory_profiler import memory_usage

# Import the sorting algorithms from separate files
from peekSort import peekSort
from radixSort import radixSort

def measureTimeAndMemoryRadix(data):
    start_time = time.perf_counter()
    memUsage = memory_usage((radixSort, (data.copy(),)))
    end_time = time.perf_counter()

    timeTakenMs = (end_time - start_time) * 1000
    maxMemory = max(memUsage) if memUsage else None
    return timeTakenMs, maxMemory

def measureTimeAndMemoryPeek(data):
    start_time = time.perf_counter()
    memUsage = memory_usage((peekSort, (data.copy(),)))
    end_time = time.perf_counter()

    timeTakenMs = (end_time - start_time) * 1000
    maxMemory = max(memUsage) if memUsage else None
    return timeTakenMs, maxMemory

def compare_algorithms(file):
    folder = 'dataset'
    pathname = os.path.join(folder, file)
    with open(pathname, 'r') as f:
        f = f.readlines()
    data = [int(line.strip()) for line in f]

    radixTime, radixMemory = measureTimeAndMemoryRadix(data)
    peekTime, peekMemory = measureTimeAndMemoryPeek(data)

    print(f"Dataset file: {file}")
    print(f"Radix Sort: Execution time = {radixTime}ms, Max Memory = {radixMemory}")
    print(f"PeekSort: Execution time = {peekTime}ms, Max Memory = {peekMemory}")


if __name__ == '__main__':
    allFiles = ['smallRandom.txt', 'smallSorted.txt', 'smallReversed.txt', 
                'mediumRandom.txt', 'mediumSorted.txt', 'mediumReversed.txt', 
                'largeRandom.txt', 'largeSorted.txt', 'largeReversed.txt']
    for file in allFiles:
        compare_algorithms(file)
        print("====================================")

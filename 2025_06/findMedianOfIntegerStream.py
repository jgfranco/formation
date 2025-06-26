
'''
You are given a list of integers read incrementally from a data stream. After each integer is read, the task is to find the median of all the integers read so far.

The median is the middle value of a sorted list of integers. If the total number of integers is even, the median is the average of the two middle elements.

Return a list of the running medians at the end.
 

EXAMPLE(S)
Examples:
Input: [1, 2, 3]
Output: [1, 1.5, 2]


[1,2,  3  ,4,8,9]   3

left           right
[1,2,3,4]       [5,8,9,10]


X=10


Explanation:
The list contains [1]. So, median = 1 / 1 = 1
The list contains [1, 2]. Median = (1 + 2) / 2 = 1.5
The list contains [1, 2, 3]. Median = 2
 



 Plan:

 - Add the current element to the max heap if it's smaller than the max heap's top element. Otherwise, add it to the min heap.
- If either heap grows larger than the other by more than 1, balance them by moving the top element from the larger heap to the smaller heap.
- The median is the middle value. If the total number of elements is even, it's the average of the two middle elements; otherwise, it's the top of the larger heap.



 
 initiate min and max heap

if num <= min_heap:
    max_heap
else
    add to min_heap

if size of min_heap+1 > max_heap:
    

FUNCTION SIGNATURE
function findMedian(arr) {}
def find_median(arr):
    max_heap = []
    min_heap = []


'''
import heapq

def findMedian(arr):
    
    result = []
    max_heap = []
    min_heap = []

    for num in arr:
        if len(max_heap) == 0: 
            heapq.heappush(max_heap, -num)
        elif num <-max_heap[0]:
            heapq.heappush(max_heap, -num)
            if len(max_heap) > len(min_heap) +1:
                val = heapq.heappop(max_heap)
                heapq.heappush(min_heap, -val)
        else:
            heapq.heappush(min_heap, num)
            if len(min_heap) > len(max_heap) +1:
                val = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -val)
        
        if len(max_heap) == len(min_heap):
            median = (-max_heap[0] + min_heap[0]) / 2
            result.append(median)
        else:
            if len(min_heap) > len(max_heap):
                median = min_heap[0]
            else:
                median = -max_heap[0]
            result.append(median)

    return result


arr = [42]
print(findMedian(arr) == [42])

arr = [5, 15, 10, 20, 3]
print(findMedian(arr)== [5, 10, 10, 12.5, 10])

arr = [1, 2, 3]
print(findMedian(arr)== [1, 1.5, 2])

arr = [-10, -5, 0, 5, 10]
print(findMedian(arr)==[-10, -7.5, -5, -2.5, 0])

arr = [10, 9, 8, 7, 6, 5]
print(findMedian(arr) ==[10, 9.5, 9, 8.5, 8, 7.5])

arr = [1, 2, 3, 4, 5, 6]
print(findMedian(arr) ==[1, 1.5, 2, 2.5, 3, 3.5])

arr = [5, 5, 5, 5, 5]
print(findMedian(arr) == [5, 5, 5, 5, 5])
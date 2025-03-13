'''
You are given a list of integers read incrementally from a data stream. After each integer is read, the task is to find the median of all the integers read so far.

The median is the middle value of a sorted list of integers. If the total number of integers is even, the median is the average of the two middle elements.

Return a list of the running medians at the end.
 
EXAMPLE(S)
Examples:
Input: [1, 2, 3]
Output: [1, 1.5, 2]

Explanation:
The list contains [1]. So, median = 1 / 1 = 1
The list contains [1, 2]. Median = (1 + 2) / 2 = 1.5
The list contains [1, 2, 3]. Median = 2

[1,2,4,6] --> 3 

FUNCTION SIGNATURE
function findMedian(arr) {}
def find_median(arr):


Explore:
- list won't be empty
- list is not sorted
- there can be duplicates

Brainstorm:
Appraoch 1:
Brute Force:
Sort it (quick sort) every time and then calculate median.

Approach 2:
- insertion sort, binary sort, selection sort, bucket sort

Approach 3:
- Max Heap for smaller nos. and min heap for larger nos.

[1,6,4,2]

min heap = we want larger elements
[6,4]. 4

max heap we want smaller elements
[1,2]. 2

(2+4)/2 = 3

minheap.size > maxheap.size > 1

Plan:
- initialize output arr
- loop through the input array:
    - add element to min heap
    - if the min heap size is > maxheap size +1:
        - pop from min heap and add to max heap
- if the min and max heap size are equal:
    - append to output arr average of minheap.pop and maxheap.pop
- append to output arr pop from whichever heap has greater num of elements
- return output

'''

#  heapq.heappush(lowerHalf, current)
# Add the current element to the max heap if it's smaller than the max heap's top element. Otherwise, add it to the min heap.

import heapq
def find_median(arr):
    result = []
    max_heap = []
    min_heap = []
    for num in arr:
        heapq.heappush(min_heap, num)
        # print(min_heap)
        # print(max_heap)
        # todo: check which heap to add to
        if num < max_heap[0]:
            heapq.heappush(max_heap, -num)
            if len(max_heap) > len(min_heap) + 1:
                val = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -val)
        else:
            heapq.heappush(min_heap, num)
            if len(min_heap) > len(max_heap) + 1:
                val = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -val)
        if len(min_heap) == len(max_heap):
            result.append((min_heap[0] -max_heap[0])/2)
        else:
            if len(min_heap) > len(max_heap):
                result.append(min_heap[0])
            else:
                result.append(-max_heap[0])
    return result

# print(find_median([1]))
print(find_median([4,5,5,2,1])) #[4,4.5,5,4.5,4] 
print(find_median([4,2,3,1])) # [4, 3, 3, 2.5]
print(find_median([5,15,1,3])) #[5,10,5,4]
print(find_median([1,2,3])) #[1,1.5,2]

print(find_median([5,4,1,2,4])) 

print(find_median([-5,-4,1,2,4])) 
'''
Given an array where each number is located less than k places away from its sorted position, fully sort the array.
 

EXAMPLE(S)
[1, 3, 4, 2, 6, 5], k = 2
returns [1, 2, 3, 4, 5, 6]

FUNCTION SIGNATURE
def k_sort(input, k)


'''
# traditional sorting is O(n * log(n)) time complexity with linear space complexity
# Can we take advantage of K to avoid doing N operations at each index and shoot for O(nlogk)?
# k given: numbers are up to k places behind or ahead of their index
# heap as a possible solution: use a minHeap to extract smallest number
# use a heap of 2 * k
# heap acts as sliding window of size (2 * k)
# move the heap by an index: smallest element on the heap will be no more than k elements away from correct index

# two-pointer approach

import heapq

def kSort(input, k):

    # create the heap of size (2 * k)
    # cover elements that are up to k places before and after their correct index

    output = []    
    heap = []
    # populate the heap
    # elements before their index are assumed to be in the correct position - popped onto output
    for i in range(k):
        heapq.heappush(heap, input[i])
    
    # run the loop to populate our heap window
    for i in range(k, len(input)):
        # add the element at this current index
        heapq.heappush(heap, input[i])
        # pop the smallest element seen on the heap
        value = heapq.heappop(heap)
        output.append(value)
        # this element is no more than k indices forwards or backwards from its correct spot - the size of the heap

    # previous loop only populates output len(input) - k times
    # window will still have elements at the end: fill output
    while heap:        
        output.append(heapq.heappop(heap))
    
    return output



def kSortWindow(array, k):

    for i in range(len(array)):
        for j in range(i+1, i+k+1):
            print(i,j)
            if j < len(array) and array[j] < array[i]:
                array[j], array[i] = array[i], array[j] 
    
    return array

print(kSortWindow([1, 3, 4, 2, 6, 5], 2))
#print(kSortWindow([5, 4, 3, 2, 1], 4))
#print(kSortWindow([5, 4, 3, 2, 1], 6))


# k = 2
#       i 
# 1, 2, 3, 4
#              j
"""
function insertIntoWindow(window, element) {
    let i = window.length - 1
    while (i >= 0 && element > window[i]) {
        window[i + 1] = window[i]
        i--
    }
    window[i + 1] = element
}

function sortNearlySorted(array, k) {
    let result = []
    let window = []

    //frontload window
    for (let i = 0; i <= k; i++) {
        insertIntoWindow(window, array[i])
    }

    for (let i = k + 1; i < array.length; i++) {
        //make room in window by popping off lowest val
        result.push(window.pop())
        //add next val to window via our insertion sort
        insertIntoWindow(window, array[i])
    }

    while (window.length > 0) {
        result.push(window.pop())
    }

    return result
}
"""

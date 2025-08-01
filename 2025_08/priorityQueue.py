import queue

def priorityQueueSort(array):
    pq = queue.PriorityQueue()
    for num in array:
        pq.put(num)

    for i in range(len(array)):
        array[i] = pq.get()

    return array

print(priorityQueueSort([]) == [])
print(priorityQueueSort([1]) == [1])
print(priorityQueueSort([2, 1]) == [1, 2])
print(priorityQueueSort([4, 2, 9, 1]) == [1, 2, 4, 9])
print(priorityQueueSort([-1, -4, 10, 3, 2]) ==  [-4, -1, 2, 3, 10])
print(priorityQueueSort([1, 1, 1, 1] ) == [1, 1, 1, 1])
print(priorityQueueSort([7, 3, -1, 0, 0, 2, 3]) == [-1, 0, 0, 2, 3, 3, 7])
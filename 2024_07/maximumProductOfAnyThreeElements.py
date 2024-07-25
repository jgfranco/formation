"""
Given an array of 5+ non zero integers. Write a function that calculates the maximum product of any 3 elements in the array

Time1: n log(N)
Time2: 0(N)
[1,2,3,4,5]
x * y * z 

[3,6,5,2,1]
[-9, -10, 10, 5, 2, 7]

[-9, -10, -10, 5, 2, 7]

largest pair of negative numbers



[-9, -10, -11, 5, 2, 7]
[-11, -10, -9, 2, 5 7]
[-2, -1, 1, 4, 10, 11]

max1 = array[-1]*array[-2]*array[-3]
max2 = array[0]*array[1]*array[-1]

find largest numbers?


function that takes an array

1. sort the array 

max1 = array[-1]*array[-2]*array[-3]
max2 = array[0]*array[1]*array[-1]

2. return max (max1, max2)



"""

def maxProductOfThree(array):

    array = sorted(array)

    max1= array[0] * array[1] *array[-1]
    max2 = array[-3]* array[-2]* array[-1]
    return  max( max1, max2)

print(maxProductOfThree([-9, -10, 10, 5, 2, 7]))
print(maxProductOfThree([1,2,3,4,5]))
print(maxProductOfThree([-10,1,2,3,4,5]))


"""
largest =
secondlargest 
thirdlargest


smallest 
secondsmallest
_ 
[-9, -10, 10, 5, 2, 7]
"""

def maxProductOfThreeNTime(array):
    largest = float("-inf")
    secondlargest = float("-inf")
    thirdlargest= float("-inf")

    smallest = float("inf")
    secondsmallest = float("inf")

    for num in array:

        if num > largest:
            largest, secondlargest, thirdlargest = num, largest, secondlargest
        elif num > secondlargest:
            secondlargest, thirdlargest = num, secondlargest
        elif num > thirdlargest: 
            thirdlargest = num

        if num < smallest:
            smallest, secondsmallest = num,  smallest
        elif num < secondsmallest:
            secondsmallest = num


    max1= smallest * secondsmallest * largest
    max2 = largest * secondlargest * thirdlargest
    return  max(max1, max2)

print(maxProductOfThreeNTime([-9, -10, 10, 5, 2, 7]))
print(maxProductOfThreeNTime([1,2,3,4,5]))
print(maxProductOfThreeNTime([-10,1,2,3,4,5]))

def maxProductOfThreeHeap(array):
    import heapq

    largest = heapq.nlargest(3, array)
    smallest = heapq.nsmallest(2, array)
  
    max1 = smallest[0] * smallest[1] * largest[0]
    max2 = largest[0] * largest[1] * largest[2]

    return max(max1, max2)

print(maxProductOfThreeHeap([-9, -10, 10, 5, 2, 7]))
print(maxProductOfThreeHeap([1,2,3,4,5]))
print(maxProductOfThreeHeap([-10,1,2,3,4,5]))
'''
Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

You must do this in O(n) runtime.
 
[2, 3, 4] => 1


EXAMPLE(S)

[1] => 2

[1, 2] => 4

[1, 2, 3] => 7


arr = 1, 2, 3, 4, 5  6, 7 

1, 2,  4 => 8
        ^

[1, 3] => 2


[2] => 1
[100] => 1


 
subsetSums = { 1, 2, 3, 4, 5 }

try every positive int beginning at 1
if INT is at index position
check is INT is in subsetsums
if not add to subSetSums
AND
create new subset sums from all other subsetsums except SELF

how do we know we found our candidate? the candidate would not be in the array AND not is the set

1 -> 2 -> 3 -> 4

[1, 2, 3, 10] => 7
 _     _

 (3+1)
          ^



subsets:
1, 2, 3, 10 = 16
1, 2, 3 = 6
2, 3, 10 = 15
1, 2 =  3
2, 3 =  5
1, 3 = 4
3, 10 = 13
        1
        2
        3 
        10


subset sums in sorted order:
1, 2, 3, 4, 5, 6,

[1, 2, 3, 4, 9] => 20
 
Questions
- what do we mean by subset?


- start with the smallest element
- if
- find the sum of all the subsets? 

FUNCTION SIGNATURE
func firstNotASum(input: [Int]) -> Int
'''

def smallest_impossible_sum(nums):

    impossible_sum = 1, 2
    for n in nums:
        if n <= impossible_sum:
            impossible_sum += n
        else:
            break
    return impossible_sum
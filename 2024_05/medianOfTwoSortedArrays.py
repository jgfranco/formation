'''
Median of Two Sorted Arrays

Given two sorted arrays, return the median of all the numbers.
 

EXAMPLE(S)
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Input: nums1 = [1, 2, 3, 4], nums2 = [5, 6, 7]
Output: 4.00000
Explanation: merged array = [1,2,3,4,5,6,7] and median is 4.
 
nums_1 = [1, 8, 10]  num_2 =  [2 , 5, 11] => 
(5+8)
13/2 = 6.5

[],[] =>
[1],[] => 1

             |                     |
nums_1 = [1, 8, 10]  num_2 =  [2 , 5, 11]
             |                     |


              x                         x
          |                              |
nums_1 = [1, 10, 11]  num_2 =  [2 , 5,  8]
              |                     |       

              |              |
nums_1 = [1, 10,11] num_2 = [3]
              |              |
[1 3 10 11]
              |              |
nums_1 = [1, 10,11] num_2 = [3, 12]
              |                  |
1 3 10 11, 12

elim smallest - 1
elim max - 11

      |
    x x
1 2 5 8 10 11
    |
when we have even numbers-> median is avg of 2 numbers in the "middle"
when we have odd number -> select the "middle" number

if right ptr crosses left ptr -> ignore ptrs 
if both ptrs point to a number on both arrays? then answer is avg of those numbers for even array



FUNCTION SIGNATURE
function findMedianSortedArrays(a, b)
'''
'''     l  r
A = [5, 6, 7] B= [1, 2, 3, 4]
        i  i1  
    al ar            bl br
 [5, 6, 7]   # Approach 1 from verbal 
 '''
def findMedianSortedArrays(A, B):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    # smaller = A bigger = B
    if len(A)>len(B):
        A,B=B,A
    total=len(A)+len(B) # 7
    half=total//2      # 3
    l,r=0,len(A)-1     # 0, 2
    while True:
        i=(l+r)//2 # 1 mid of A    0 
        j=half-i-2 # 3-1-2 = 0     1
        print(f" i:{i} j: {j}")
        ALeft=A[i] if i>=0 else float("-infinity")
        ARight=A[i+1] if (i+1)<len(A) else float("infinity")
        BLeft=B[j] if j>=0 else float("-infinity")
        BRight=B[j+1] if (j+1)<len(B) else float("infinity")
        print(f"AL:{ALeft} AR:{ARight} BL: {BLeft} BR:{BRight} \n")
        
        if ALeft<=BRight and BLeft<=ARight:
            if total%2!=0:
                return min(ARight,BRight)
            else:
                return (max(ALeft,BLeft) + min(ARight,BRight))/2
        if ALeft>BRight:
            r=i-1
            # print(f"{r}")
            # break
        else :
            l=i+1

findMedianSortedArrays([5,6,7],[1,2,3,4])
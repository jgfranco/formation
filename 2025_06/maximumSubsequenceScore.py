
"""
2542. Maximum Subsequence Score
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.

For chosen indices i0, i1, ..., ik - 1, your score is defined as:

The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
Return the maximum possible score.

A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.

 

Example 1:

Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12
Explanation: 
The four possible subsequence scores are:
- We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
- We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
- We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
- We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
Therefore, we return the max score, which is 12.
Example 2:

Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
Output: 30
Explanation: 
Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.
"""

def maxScore(nums1: list[int], nums2: list[int], k: int) -> int:

    import heapq
    total = result = 0

    heap = []

    pairs = sorted(list(zip(nums1, nums2)), key = lambda x: -x[1])

    for a,b in pairs:
        heapq.heappush(heap, a)
        total += a
        if len(heap) > k:
            total -= heapq.heappop(heap)
        if len(heap) == k:
            result = max(result, total * b)

    return result

case1 = ([1,3,3,2], [2,1,3,4], 3, 12)
case2 = ([4,2,3,1,1], [7,5,10,9,6], 1, 30)
cases = [case1, case2]

for case in cases:
    nums1,  nums2, k, expected = case

    result = maxScore(nums1, nums2, k)

    if result != expected:
        print(f'test failed, expected: {expected}, actual: {result}')
    if result == expected:
        print(f'test passed, expected: {expected}, actual: {result}')


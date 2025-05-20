
"""
https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        
        import heapq

        heap = []

        for num in nums:
            heapq.heappush(heap, -num)

        for i in range(k-1):
            heapq.heappop(heap)
        
        return -heap[0]

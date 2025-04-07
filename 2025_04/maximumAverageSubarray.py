"""
https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10^-5 will be accepted.
Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75


"""

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        """

        sliding window approach:
        keep track of the max value so far
        we traverse the first window to calculate its sum

        from that moment on
        we slide the window:
        we substract the first element and add to to sum the next element
        """

        if len(nums) < k: return 0

        left = 0
        right = k - 1
        maxSum = float('-inf')
        currentSum = 0
        while right < len(nums):
            if left == 0:
                currentSum = sum(nums[left:right + 1])
            else:
                currentSum -= nums[left - 1]
                currentSum += nums[right]

            maxSum = max(maxSum, currentSum)
            left += 1
            right += 1
        return maxSum / k
    
# Test cases

if __name__ == "__main__":
    s = Solution()
    print(s.findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # Expected output: 12.75
    print(s.findMaxAverage([5], 1))                    # Expected output: 5.0
    print(s.findMaxAverage([-1, -2, -3, -4], 2))      # Expected output: -1.5
    print(s.findMaxAverage([0, 0, 0], 2))              # Expected output: 0.0


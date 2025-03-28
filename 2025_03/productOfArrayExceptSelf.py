
'''
https://leetcode.com/problems/product-of-array-except-self/submissions/1587333945/?envType=study-plan-v2&envId=leetcode-75'
'''
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        products = [1] * length
        
        for i in range(1, length):
            products[i] = products[i-1] * nums[i-1]

        
        right = nums[-1]
        for i in range(length-2, -1, -1):
            products[i] *= right
            right *= nums[i]
        
        return products
    

print(Solution().productExceptSelf([1,2,3,4])) # [24,12,8,6]
print(Solution().productExceptSelf([-1,1,0,-3,3])) # [0,0,9,0,0]


"""
https://leetcode.com/problems/asteroid-collision/description/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

    
        for asteroid in asteroids: #[10] __ -5
            while stack and stack[-1] >= 0 and asteroid < 0:
                if stack[-1] < abs(asteroid): # current asteroid is larger
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(asteroid): # 
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        
        return stack

s = Solution()
 
print(s.asteroidCollision([10,2,-5]))

        
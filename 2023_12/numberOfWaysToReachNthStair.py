'''
Given an input N representing n number of stairs, compute the number of ways to reach the n'th stair if you can climb either 1 or 2 stairs at a time.
 

EXAMPLE(S)
Input: 1
Output: 1
Explanation: There is only one way to climb one stair: (1)

Input: 2
Output: 2
Explanation: There are 2 ways to climb 2 stairs: (1,1) and (2)

Input: 4
Output: 5
Explanation: Here are the ways to climb 4 stairs: (1,1,1,1), (1,1,2), (1,2,1), (2,2)
 

FUNCTION SIGNATURE
func numWaysToClimb(input: n) -> Int

'''
'''
steps = 4
            1               2
        1       2
    1
1
'''
# Time (2/\n)
#                  4
          
#tracker = {steps: ways}

def numWaysToClimb(steps):
    if steps == 0: return 0
    tracker = {}
                # 2
    def helper(currentSum):

        if currentSum in tracker:
            return tracker[currentSum]
            
        if currentSum > steps:
            return 0

        if currentSum == steps:
            return 1

    
        tracker[currentSum] = helper(currentSum+1) + helper(currentSum+2)
        return tracker[currentSum]

    #helper(0)

    return helper(0)

print(numWaysToClimb(0))
print(numWaysToClimb(1))
print(numWaysToClimb(2))
print(numWaysToClimb(4))

'''
1 = 0
2 = 1
3 = 1
4 = 2
                        4
                    f(3) + f(2) 
                f(2) + f(1)    f(1)


public class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
}
'''

#dp[3] =


# dp = {}
# dp[1] = 1

# 2 to n+1
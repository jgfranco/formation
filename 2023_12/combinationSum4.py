



class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        nums.sort()

        dp = [0 for i in range(target+1)]
        dp[0] = 1
        print(dp)

        # nums = [1,2,3]
        # target = 4
        # dp[0] = 1
        # dp[1] = 0->1
        # dp[2] = 0->1->2
        # dp[3] = 0->2->3->4
        # dp[3] = 0->4->6->7
        #                                              _
        for comb_sum in range(target+1): # 0, 1, 2, 3, 4
            #                        _
            for num in nums: # 1, 2, 3
                print(comb_sum, num)
                if comb_sum - num >= 0: # 1
                    dp[comb_sum] += dp[comb_sum - num]
                else:
                    break

        return dp[target]


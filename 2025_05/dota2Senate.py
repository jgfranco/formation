"""
https://leetcode.com/problems/dota2-senate/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque

        RSenators = deque([])
        DSenators = deque([])
        n = len(senate)

        for idx,senator in enumerate(senate):
            if senator == "R":
                RSenators.append(idx)
            else:
                DSenators.append(idx)

        while len(RSenators)> 0 and len(DSenators)>0:
            if RSenators[0] < DSenators[0]:
                DSenators.popleft()
                RSenators.append(RSenators.popleft() + n)
            else: 
                RSenators.popleft()        
                DSenators.append(DSenators.popleft() + n)

        if len(RSenators) > 0: return "Radiant"

        return "Dire"
    

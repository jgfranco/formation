"""
https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75"
"""
class Solution:
    def compress(self, chars: list[str]) -> int:
    
        p = 0
        res = 0
        length = len(chars)
        while p < length:
            counter = 1
            while p + counter < length and chars[p + counter] == chars[p]:
                counter += 1
            
            chars[res] = chars[p]
            res +=1
            if counter > 1:
                count = str(counter)
                chars[res: res + len(count)] = list(count)
                res += len(count)
            p += counter
        
        return res
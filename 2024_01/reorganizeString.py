"""
767. Reorganize String

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters."""

import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        charFreq = {}
        for char in s:
            charFreq[char] = charFreq.get(char, 0) +1

        maxHeap = [(-freq, char) for char, freq in charFreq.items()]
        heapq.heapify(maxHeap)

        print(maxHeap)

        res = []
        prevFreq, prevChar = 0, ""

        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            res.append(char)
            
            if prevFreq < 0:
                heapq.heappush(maxHeap, (prevFreq, prevChar))
            
            freq +=1
            prevFreq, prevChar= freq, char

        if len(res) != len(s): return ""

        return "".join(res)
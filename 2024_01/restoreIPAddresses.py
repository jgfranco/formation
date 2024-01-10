"""
https://leetcode.com/problems/restore-ip-addresses/
93. Restore IP Addresses
Medium

5053

776

Add to List

Share
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
"""

class Solution:
  def restoreIpAddresses(self, s: str):
    # keep track of how many dots i have introduced into the string
    # input should be between 4 and 12 characters in lenght, otherwise we cannot process the string

    if 4 < len(s) > 12: return [] 
    
    result = []
    
    def isValid(integer):
      if integer == "": return False
      if len(integer) > 1 and integer[0] == "0": return False
      if len(integer) > 3: return False
      if int(integer) > 255: return False
      
      return True
    
    def restoreIPAddressesHelper(stringSoFar, dotsAssigned, pointer, currentInteger):
      if pointer >= len(s): 
        if dotsAssigned ==3 and isValid(currentInteger):
          result.append(stringSoFar)
        return 
      
      if isValid(currentInteger):
        restoreIPAddressesHelper(stringSoFar+ ".", dotsAssigned+1, pointer, "") 
      
      restoreIPAddressesHelper(stringSoFar +s[pointer], dotsAssigned, pointer +1, currentInteger+s[pointer] )

    restoreIPAddressesHelper("", 0, 0, "")

    return result
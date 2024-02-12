
"""
Q. Given a string, reverse it by character blocks of k.

Examples:

Input: string = "Formation", k = 3
Output: "roFtamnoi"  // Since k is 3, divide the string by a block of 3 characters: "For", "mat", and "ion" and reverse it by blocks.

If k doesn't evenly divide, just reverse last block left.
Input: string = Fellow, k = 4
Output: "lleFwo" // "Fell" and "ow"

If k exceeds the length of the array, do nothing.
Input: string = "Fellow, k = 7
Output: "Fellow"
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string string

[input] integer k

[output] string

"""
def reverseStringInChunks(string, k):
    if k <=1 or k > len(string): return string
    newString = ""

    for i in range (0, len(string), k):
        #print(string[i::-1])
        sub = string[i: i+k]
        newString += sub[:: -1]
        
    return newString


print(reverseStringInChunks("Formation", 3))
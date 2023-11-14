class Test:
    def __init__(self, test_name = ""):
        self.total_count = 0
        self.problem_count = 0
        self.total_score = 0
        self.problem_score = 0
        self.current_problem = ""
        self.failed_problems = []
        print(f"Beginning Test: {test_name}")
        
    # Test Helpers
    def test(self, expected_outcome, outcome, case_num = 0):
        if expected_outcome == outcome:
            return self.passed(case_num)
        return self.failed(case_num)  

    def testMultipleCases(self, possible_outcomes, outcome, case_num = 0):
        for possible_outcome in possible_outcomes:
            if possible_outcome == outcome:
                return self.passed(case_num)
        return self.failed(case_num)

    def testMatchAny(self, expected_outcome, outcome, case_num = 0):
        if self.isEqual(expected_outcome, outcome):
            return self.passed(case_num)
        return self.failed(case_num)        

    def isEqual(self, array1, array2) -> bool:
        for a1 in array1:
            a1.sort()
        sortedArray1 = sorted(array1)
        for a2 in array2:
            a2.sort()
        sortedArray2 = sorted(array2)
        return sortedArray1 == sortedArray2 
    
    # Test Logistics
    def startProblem(self, problemName):
        self.current_problem = problemName
        self.problem_score = 0
        self.problem_count = 0
        self.failed_problems = []
    def passed(self, case_num):
        self.total_score += 1
        self.problem_score += 1
        self.problem_count += 1
        self.total_count += 1
    def failed(self, case_num): 
        self.problem_count += 1
        self.total_count += 1
        self.failed_problems.append(case_num)

    def endProblem(self):
        print(f"\n   {self.current_problem} Score: {self.problem_score} / {self.problem_count}")
        if len(self.failed_problems) > 0:
            print(f"   ** Failed Test Cases: {self.failed_problems}")
    def printFinal(self):
        print(f"\nTotal Score: {self.total_score} / {self.total_count}")

test = Test("")

class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next
        
def arrayify(head) -> list[int]:
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array

class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
def arrayifyTree(root: TreeNode):
    if root is None:
        return []
    queue = []
    array = []
    queue.append(root)
    while (len(queue) != 0):
        node = queue.pop(0)
        array.append(node.value)
        if (node.left):
            queue.append(node.left)
        if (node.right):
            queue.append(node.right)
    return array

from typing import List

'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given two strings, return the minimum number of operations to edit the first string to get the second string. Three operations to consider are:
      1. insertion of a character
      2. deletion of a character
      3. substitution of a character for another 

Examples:
• Given strings: str1 = "abc", str2 = "ab" // returns 1
• Possible operations: delete "c"
• Given strings: str1 = "abc", str2 = "c" // returns 2
• Possible operations: delete "a", delete "b"

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
0 1 2 3 4
1 0 0 0 0
2 0 0 0 0
3 0 0 0 0

'''
def levenshteinDistance(str1, str2):
  m, n = len(str1), len(str2)
  dp = [[0] * (n + 1) for _ in range(m + 1)]
    
  for i in range(m + 1):
    dp[i][0] = i
  for j in range(n + 1):
    dp[0][j] = j
    
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if str1[i - 1] == str2[j - 1]:
        dp[i][j] = dp[i - 1][j - 1]
      else:
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

  return dp[m][n]

# Test Cases
test.startProblem("Levenshtein Distance")
test.test(1, levenshteinDistance("abc", "adbc"), 1)
test.test(10, levenshteinDistance("formation", "buildschool"), 2)
test.test(0, levenshteinDistance("", ""), 3)
test.test(0, levenshteinDistance("coding", "coding"), 4)
test.test(5, levenshteinDistance("apple", "pineApple"), 5)
test.test(10, levenshteinDistance("af12312fasfesf", "afase1iu3wfuwi"), 6)
test.endProblem()
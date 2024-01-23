"""
207. Course Schedule
https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""


class Solution:
  def canFinish(self, numCourses, prerequisites) -> bool:
    indegree = [0] * numCourses
    adjList = {i:[] for i in range(numCourses)}
    
    for a,b in prerequisites:
      adjList[b].append(a)
      indegree[a] += 1
        
    from collections import deque
    q = deque([])
    for i, val in enumerate(indegree):
      if val == 0:
        q.append(i)
          
    coursesTaken = 0
    while q:
      course = q.popleft()
      coursesTaken +=1
      for dependantCourse in adjList[course]:
        indegree[dependantCourse] -=1
        if indegree[dependantCourse] == 0:
          q.append(dependantCourse)
    
    return coursesTaken == numCourses
                
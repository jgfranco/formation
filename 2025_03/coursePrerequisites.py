
'''
Suppose you're a school headmaster and somebody has drafted a course list for a new program. Each course has an ID associated with it, and they may have prerequisites.

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where each entry is a pair of course numbers, [c, prq], indicates that you must take course prq first if you want to take course c.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Given the number of courses, numCourses, and the list of prerequisites, return true if you can finish all courses. Otherwise, return false.
 

EXAMPLE(S)
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

FUNCTION SIGNATURE
function courseSchedule(numCourses, prerequisites)


find sources, finding the courses that have no prerequisites

stack = [s1, s2]

indegree 
                    Z 0
                   /
           A.   G 1
          /   /
        B1    C 2

using a map keep of track of indegree

'''

from collections import deque

def courseSchedule(numCourses, prerequisites):

    indegree = {}
    adjecency = {}
    q = deque([])


    for i in range(0, numCourses):
        indegree[i] = 0
        adjecency[i] = []

    for relationship in prerequisites:
        c = relationship[0]
        p = relationship[1]
        indegree[c] += 1
        adjecency[p].append(c)

    for c,ind in indegree.items():
        if ind ==0:
            q.append(c)

    while q:
        source = q.popleft()
        numCourses -= 1

        for course in adjecency[source]:
            indegree[course] -= 1
            if indegree[course] == 0:
                q.append(course)

    return numCourses == 0

print(courseSchedule(2, [[0,1]])) # True
print(courseSchedule(2, [[1,0],[0,1]])) # False
print(courseSchedule(2, [[0,1],[1,0]])) # False
print(courseSchedule(3, [[0,1],[0,2],[1,2]])) # True


#         indegree = [0] * numCourses
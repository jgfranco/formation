'''
https://leetcode.com/problems/rectangle-overlap/

836. Rectangle Overlap

An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

🔎 EXPLORE
What are some other insightful & revealing test cases?

case 1
a [1,1,2,2]
b [3,3,5,5]
5         b
4          
3     b  
2   a
1 a
0 1 2 3 4 5

return False

case 2
a [1,1,3,3]
b [3,3,5,5]
5         b
4          
3     ab  
2   
1 a
0 1 2 3 4 5

return False

case 3
a [1,1,3,3]
b [2,2,5,5]
5         b
4          
3     a  
2   b
1 a
0 1 2 3 4 5

return True

🧠 BRAINSTORM
What approaches could work?
get the edges (left, right, down and up ) of the overlapping area 
Algorithm 1:
Time: O(1)
Space: O(1)
 

📆 PLAN
Outline of algorithm #:
get left of overlapping area
get right of overlapping area
get top of overlapping area
get bottom of overlapping area

if left is larger or equal to right return False
if bottom is larger or equal to top return False

return True 

 

🛠️ IMPLEMENT
Write your algorithm.
'''
def isRectangleOverlap(rec1, rec2):

  left = max(rec1[0], rec2[0])
  right = min(rec1[2], rec2[2])
  bottom = max(rec1[1], rec2[1])
  top = min(rec1[3], rec2[3])

  if left >= right or bottom >=top: return False

  return True
'''

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

rec1 = [1,1,2,2]
rec2 = [3,3,5,5]

print(isRectangleOverlap(rec1, rec2), "expect False")

rec1 = [1,1,3,3]
rec2 = [3,3,5,5]

print(isRectangleOverlap(rec1, rec2), "expect False")


rec1 =  [1,1,3,3]
rec2 =  [2,2,5,5]

print(isRectangleOverlap(rec1, rec2), "expect True")
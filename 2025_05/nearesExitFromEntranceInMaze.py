

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        def isExit(x, y):

            if [x,y] == entrance:
                return False

            if x == 0 or y == 0 or x == len(maze)-1 or y == len(maze[0])-1:
                return True
            return False

        def validSteps(x, y):
            validSteps = []
            if x + 1 < len(maze) and maze[x+1][y] == ".":
                validSteps.append((x+1, y))
            if x - 1 >= 0 and maze[x-1][y] == ".":
                validSteps.append((x-1, y))
            if y + 1 < len(maze[0]) and maze[x][y+1] == ".":
                validSteps.append((x, y+1))
            if y - 1 >= 0 and maze[x][y-1] == ".":
                validSteps.append((x, y-1))

            return validSteps
            
        steps = 0
        
        from collections import deque

        q = deque([entrance])

        while q:
            size = len(q)

            for _ in range(size):
                x,y = q.popleft()
                if isExit(x,y):
                    return steps
               
                vSteps = validSteps(x,y)
                for step in vSteps:
                    q.append(step)
                    maze[step[0]][step[1]] = "+"

            steps += 1

        return -1
                





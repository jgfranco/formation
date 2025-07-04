
# Definition for a Node.
class Node:
    def __init__(self, val= None, children = None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root) -> list[int]:
        if not root: return []

        stack= [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)

            stack.extend(reversed(node.children))
        
        return result
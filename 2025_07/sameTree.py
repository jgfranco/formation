from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class NTreeNode:
    def __init__(self, val=0, children = []):
        self.val = val
        self.children = children

# recursive approach
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not q and not p: return True
    if not q or not p: return False
    if q.val != p.val: return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# iterative approach
def isSameTreeIterative(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

    if not p and not q: return True
    if not p or not q: return False
    from collections import deque
    pqdeque = deque([(p,q)])


    while pqdeque:
        pNode, qNode = pqdeque.popleft()

        # *** commented check to honor follow up number 2
        #if pNode.val != qNode.val:
            #return False

        if pNode.left and qNode.left:
            pqdeque.append((pNode.left, qNode.left))
        elif pNode.left or qNode.left: return False
        
        if pNode.right and qNode.right:
            pqdeque.append((pNode.right, qNode.right))
        elif pNode.right or qNode.right:
            return False
    
    return True
            
# n-ary trees 
def isSameTreeNary(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

    if not p and not q: return True
    if not p or not q: return False
    from collections import deque
    pqdeque = deque([(p,q)])


    while pqdeque:
        pNode, qNode = pqdeque.popleft()

        if pNode.val != qNode.val:
            return False

        if len(pNode.children) != len(qNode.children): return False

        for i in range(len(pNode.children)):
            pqdeque.append((pNode.children[i], qNode.children[i]))
        

    return True

# Python test suite for isSameTree

def build_tree(arr):
    """Builds a binary tree from a level-order list representation."""
    if not arr:
        return None
    nodes = [None if val is None else TreeNode(val) for val in arr]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root

# Replace this with your own implementation
# def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#     pass

cases = [
    ([1,2,3], [1,2,3], True),            # identical trees
    ([1,2], [1,None,2], False),           # structural difference
    ([1,2,1], [1,1,2], False),            # value difference
    ([], [], True)                        # both empty
]

for i, (a, b, expected) in enumerate(cases, 1):
    print("recursive approach")
    result = isSameTree(build_tree(a), build_tree(b))
    print(f'Test {i}: {result} (expected {expected})')

    print("iterative approach")
    result = isSameTreeIterative(build_tree(a), build_tree(b))
    print(f'Test {i}: {result} (expected {expected})')


# n-ary test

naryTree1 = NTreeNode(1, [NTreeNode(2), NTreeNode(3), NTreeNode(4)])
naryTree2 = NTreeNode(1, [NTreeNode(2), NTreeNode(3), NTreeNode(4)]) 
naryTree3 = NTreeNode(1, [NTreeNode(2), NTreeNode(3), NTreeNode(5)]) 
naryTree4 = NTreeNode(1, [NTreeNode(2), NTreeNode(3)]) 


print(isSameTreeNary(naryTree1, naryTree2), "expect True") # identical trees 
print(isSameTreeNary(naryTree1, naryTree3), "expect False") # value difference
print(isSameTreeNary(naryTree1, naryTree4), "expect False") # structural differences
print(isSameTreeNary(None,naryTree1), "expect False") # one empty
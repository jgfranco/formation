class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def find_element_in_bst(node, target):
    while node:
        if node.val == target:
            return True
        if node.val < target:
            node = node.right
        else:
            node = node.left

    return False

# Test case 1: Element is present in the tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
assert find_element_in_bst(root, 15) == True

# Test case 2: Element is not present in the tree
assert find_element_in_bst(root, 20) == False

# Test case 3: Element is the root
assert find_element_in_bst(root, 10) == True

# Test case 4: Empty tree
assert find_element_in_bst(None, 10) == False

# Test case 5: Single element tree
single_node = TreeNode(7)
assert find_element_in_bst(single_node, 7) == True
assert find_element_in_bst(single_node, 8) == False
# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str

        [1, [2, None, None],[3, 4,5]]

        [1,[2,4,5], 3]

        [1, 2, None] # 2 is left child
        [1, None, 3] # 3 is right hild
        """
        result = []

        def DFS(root):
            if not root: 
                result.append('None')
                return 
            
            result.append(str(root.val))
            DFS(root.left)
            DFS(root.right)
        
        DFS(root)
        print(result)
        return ",".join(result)
        
        



        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        data = data.split(',')
        print(data)
        self.index = 0
    
        def DFS():
            if data[self.index] == "None":
                self.index +=1
                return None
            
            root = TreeNode(int(data[self.index]))
            self.index +=1
            root.left = DFS()
            root.right = DFS()
            return root
        
        return DFS()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))a
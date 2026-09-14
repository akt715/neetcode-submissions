# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serializedArr = []
        def dfs(root):
            if not root:
                serializedArr.append('None')
                return 
            serializedArr.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(serializedArr)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        dataArr = data.split(",")
        index = [0*1]
        def dfs():
            if dataArr[index[0]]=='None':
                index[0]+=1
                return None
            
            root = TreeNode(int(dataArr[index[0]]))
            index[0]+=1
            root.left  = dfs() 
            root.right = dfs()
            return root
        return dfs()



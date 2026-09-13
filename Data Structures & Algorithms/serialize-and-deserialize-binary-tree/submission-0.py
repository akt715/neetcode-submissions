# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque()
        q.append(root)
        serializedStr = []
        if not root :
            return ""
        serializedStr.append(str(root.val))
        while q:
            temp = q.popleft()
            if temp.left:
                serializedStr.append(str(temp.left.val))
                q.append(temp.left)
            else: 
                serializedStr.append("None")
            

            if temp.right:
                serializedStr.append(str(temp.right.val))
                q.append(temp.right) 
            else:
                serializedStr.append("None")
               
           
        return ",".join(serializedStr)


    def deserialize(self, data: str) -> Optional[TreeNode]:
         q=deque()
         i= 1
         print(data)
         dataArr = data.split(',')
         root = TreeNode(dataArr[0])
         
         q.append(root)
         while q:
           if i > len(dataArr)-1:
              break
           temp = q.popleft()
           if dataArr[i] != "None":
              temp.left = TreeNode(int(dataArr[i]))
              q.append(temp.left)           
           i+=1
           if dataArr[i] != "None":
              temp.right = TreeNode(int(dataArr[i]))
              q.append(temp.right)
           i+=1

           

         return root
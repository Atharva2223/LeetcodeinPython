# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,node,level_size,ans):

        if node is None:
            return 
        
        if len(ans) == level_size:
            ans.append(node.val)
       
        self.solve(node.right,level_size+1,ans)
        self.solve(node.left,level_size+1,ans)
        


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans= []
        self.solve(root,0,ans)
        return ans


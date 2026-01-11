# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution:
    def Tilt(self,root:Optional[TreeNode]) -> int:
        if not root :
            return 0
    
        leftSum = self.Tilt(root.left)
        rightSum = self.Tilt(root.right)
        self.total += abs(leftSum-rightSum)
    
        return  leftSum + rightSum + root.val
    
    
    def findTilt(self,root:Optional[TreeNode]) -> int:
        self.total = 0
        self.Tilt(root)
        return self.total
    
    
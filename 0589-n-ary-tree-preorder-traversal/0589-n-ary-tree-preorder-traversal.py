"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

        
class Solution:
    def __init__(self):
        self.preorderList = []
    def Traversal(self,root:Optional['Node']):
        if not root :
            return
        self.preorderList.append(root.val)

        for i in root.children or []:
            self.Traversal(i)
        
    def preorder(self,root:'Node') -> List[int]:
        self.Traversal(root)
        return self.preorderList
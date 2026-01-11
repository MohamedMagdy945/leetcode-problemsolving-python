class Solution:
    def intersection(self,nums1:List[int],nums2: List[int]) -> List[int]:
        st1 = set(nums1)
        st2 = set(nums2)
        
        solve = set()
        for i in st1:
            if (i in st2):
                solve.add(i)
                
        return list(solve)
    
    
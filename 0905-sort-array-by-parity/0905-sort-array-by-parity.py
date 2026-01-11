class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        low = 0
        last = len(nums) - 1
        while low < last :
            if nums[low] % 2 == 0  :
                low += 1
            elif nums[last] % 2 != 0 :
                last -= 1
            else:
                nums[low],nums[last] = nums[last],nums[low]
                low += 1
                last -= 1
        return nums
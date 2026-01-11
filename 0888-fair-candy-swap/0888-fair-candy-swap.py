class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        bobCandy = set(bobSizes)
        sumaliceSizes= sum(aliceSizes)
        sumbobSizes = sum(bobSizes)
        swapedCandy = []
        for i in aliceSizes:
            j = (sumbobSizes-sumaliceSizes) // 2 + i
            if j in bobCandy:
                swapedCandy.append(i)
                swapedCandy.append(j)
                return swapedCandy
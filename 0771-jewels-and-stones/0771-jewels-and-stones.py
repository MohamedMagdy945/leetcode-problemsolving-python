class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelTypes = set(jewels)
        jewelStoneNumber = 0
        for ch in stones:
            if ch in jewelTypes:
                jewelStoneNumber += 1
        return jewelStoneNumber

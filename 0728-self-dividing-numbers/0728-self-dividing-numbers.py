class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        def isSelfDividing(num: int) -> bool:
            original = num
            while num > 0:
                digit = num % 10 
                if digit == 0 or original % digit != 0:
                    return False
                num //= 10  
            return True
        for n in range(left, right + 1):
            if isSelfDividing(n):
                result.append(n)

        return result
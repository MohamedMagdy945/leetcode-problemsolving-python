class Solution:
  def findTheDifference(self, s: str, t: str) -> str:
        charCount = {}
        for char in t:
            charCount[char] = charCount.get(char, 0) + 1
        for char in s:
            charCount[char] -= 1
            
        for char in charCount:
            if charCount[char] > 0:
                return char

        return ""
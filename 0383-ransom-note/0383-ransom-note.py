class Solution:
    def canConstruct(self, ransomNote: str , magazine: str) -> bool:
        counterMagazine = Counter(magazine)
        for i in ransomNote :
            if counterMagazine[i] > 0 :
                counterMagazine[i] -= 1
            else:
                return False
        return True
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower()
        banned_set = set(banned)
        
        for ch in string.punctuation:
            paragraph = paragraph.replace(ch, " ")
        
        words = paragraph.split()
        
        wordCount = {}
        max_count = 0
        answer = ""
        
        for w in words:
            if w not in banned_set:
                wordCount[w] = wordCount.get(w, 0) + 1
                if wordCount[w] > max_count:
                    max_count = wordCount[w]
                    answer = w
        
        return answer

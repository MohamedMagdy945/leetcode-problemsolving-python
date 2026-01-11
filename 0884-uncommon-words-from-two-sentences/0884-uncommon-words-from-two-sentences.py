class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split()
        words2 = s2.split()

        count1 = Counter(words1)
        count2 = Counter(words2)

        result = []

        for word, freq in count1.items():
            if freq == 1 and word not in count2:
                result.append(word)

        for word, freq in count2.items():
            if freq == 1 and word not in count1:
                result.append(word)

        return result
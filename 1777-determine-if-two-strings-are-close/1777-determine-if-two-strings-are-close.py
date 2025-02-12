class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        n1 = Counter(word1)
        n2 = Counter(word2)
        return sorted(n1.values()) == sorted(n2.values())
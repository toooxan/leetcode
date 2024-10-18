class Solution:
    def reverseVowels(self, s: str) -> str:
        s1 = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        l, r = 0, len(s) - 1
        while l < r:
            if s1[l] not in vowels:
                l += 1
            elif s1[r] not in vowels:
                r -= 1 
            else:
                s1[r], s1[l] = s1[l], s1[r]
                l += 1
                r -= 1
        return ''.join(s1)
            
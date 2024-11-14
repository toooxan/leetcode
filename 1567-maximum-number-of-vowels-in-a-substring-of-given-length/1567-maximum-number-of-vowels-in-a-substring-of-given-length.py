class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = 0
        max_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                vowel_count += 1
        max_vowels = vowel_count

        for i in range(k, len(s)):
            if s[i-k] in vowels:
                vowel_count -= 1
            if s[i] in vowels:
                vowel_count += 1
            max_vowels = max(max_vowels, vowel_count)
        return max_vowels
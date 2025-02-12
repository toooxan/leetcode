class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        current = 0
        for i in gain:
            current += i
            max_alt = max(current, max_alt)
        return max_alt
        
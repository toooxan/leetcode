class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        occ = list(count.values())
        return len(occ) == len(set(occ))
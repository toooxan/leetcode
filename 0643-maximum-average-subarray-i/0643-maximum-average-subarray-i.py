class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_sum = sum(nums[:k])
        current = max_sum
        for i in range(k, n):
            current += nums[i] - nums[i - k]
            max_sum = max(max_sum, current)

        return max_sum / k
        
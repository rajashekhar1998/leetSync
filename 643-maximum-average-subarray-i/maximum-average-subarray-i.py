class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # using sliding window technique
        left = 1
        right = k
        
        total = sum(nums[:k])
        max_sum = total

        for i in range(k, len(nums)):
            total = total - nums[left-1] + nums[right]
            max_sum = max(total, max_sum)
            left += 1
            right += 1

        return max_sum/k
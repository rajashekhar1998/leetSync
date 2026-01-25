class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)

        left_sum = 0
        right_sum = total_sum

        for i, value in enumerate(nums):
            if left_sum == total_sum - left_sum - value:
                return i
            left_sum = left_sum + value

        return -1

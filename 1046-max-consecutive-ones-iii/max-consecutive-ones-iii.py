class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        result = 0
        left = 0
        count = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                count = count + 1

            while count > k:
                # slide left pointer right till we find zero as limit reached
                if nums[left] == 0:
                    count = count -1
                left = left + 1

            length = right - left + 1
            result = max(length, result)

        return result
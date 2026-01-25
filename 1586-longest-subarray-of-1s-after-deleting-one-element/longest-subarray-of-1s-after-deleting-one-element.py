class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        #jut like the longest subarray by flipping zero's
        # here we have to do the same and max length -1 
        no_of_zeros_allowed = 1
        left = 0
        result = 0
        count = 0

        for right in range(len(nums)):
            
            if nums[right] == 0:
                count = count +1 

            while count > no_of_zeros_allowed:
                if nums[left] == 0:
                    count = count -1
                left = left +1

            length = right - left +1
            result = max(result, length)

        return result -1
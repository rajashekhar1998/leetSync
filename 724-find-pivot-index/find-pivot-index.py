class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # create left sum array of length n
        # traverse from right calculating sum to find the position.

        k = len(nums)
        right_sum_array = [None] * k
        right_sum_array = [None] * k

        left_sum = 0
        right_sum = 0

        n = k

        while n > 0:
            right_sum_array[n-1] = right_sum
            right_sum = right_sum + nums[n-1]
            n = n-1
        
        n = 0

        while n < k:
            if left_sum == right_sum_array[n]:
                return n
            left_sum = left_sum + nums[n]
            n = n +1

        return -1
            

        



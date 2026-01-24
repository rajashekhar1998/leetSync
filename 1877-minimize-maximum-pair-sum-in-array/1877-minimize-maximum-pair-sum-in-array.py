class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        # Step 1: Sort the array to access elements greedily
        nums.sort()
    
        max_pair_sum = 0
        n = len(nums)
    
        # Step 2: Use two pointers to pair smallest with largest
        for i in range(n // 2):
            current_sum = nums[i] + nums[n - 1 - i]
            # Step 3: Track the highest sum seen so far
            max_pair_sum = max(max_pair_sum, current_sum)
        
        return max_pair_sum
        
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        largest_sum = nums[0]
        
        for i in range(1, len(nums)):
            if (curr_sum + nums[i] > nums[i]):
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]
            if (curr_sum > largest_sum):
                largest_sum = curr_sum
        return largest_sum
        

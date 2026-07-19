class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        maxEnd = nums[0]

        for i in range(1, len(nums)):
            maxEnd = max(maxEnd + nums[i], nums[i])
            result = max(result, maxEnd)

        return result
        

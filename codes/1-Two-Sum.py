class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            x = list(filter(lambda x:(x + nums[i])==target, nums[i+1:]))
            if len(x) == 1:
                return [i, i+1+nums[i+1:].index(x[0])]

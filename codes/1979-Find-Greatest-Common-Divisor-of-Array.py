class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallNum = min(nums)
        largeNum = max(nums)
        while largeNum % smallNum != 0:
            largeNum, smallNum = smallNum, largeNum % smallNum
        return smallNum

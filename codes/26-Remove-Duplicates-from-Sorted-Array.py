class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        flag = False
        for m in range(1,len(nums)):
            if flag: 
                break
            flag = True
            for i in range(1,len(nums)):
                if nums[i] == nums[i-1]:
                    flag = False
                    nums.pop(i)
                    k -= 1
                    break
        
        return k

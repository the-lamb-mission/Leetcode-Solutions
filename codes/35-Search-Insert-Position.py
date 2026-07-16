class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        lB = 0
        uB = len(nums)-1
        mid = (lB+uB) >> 1
        print(lB, uB, mid) 

        while lB < uB:
            if nums[mid] > target:
                uB = max(mid - 1, lB)
            elif nums[mid] < target:
                lB = min(mid + 1, uB)
            else:
                return mid
            mid = (lB+uB) >> 1 
        
        return mid + 1 if target > nums[mid] else mid

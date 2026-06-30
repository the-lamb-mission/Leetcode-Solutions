class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1+nums2
        a.sort()
        print(a, round((len(a))/2))
        if len(a)%2==0:
            return (a[round(len(a)/2)]+a[round(len(a)/2)-1])/2
        return a[len(a)//2]
        

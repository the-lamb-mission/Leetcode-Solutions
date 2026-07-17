class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        newIntervals = [intervals.pop(0)]
        for interval in intervals:
            if interval[0] <= newIntervals[-1][1]:
                newIntervals[-1][1] = max(newIntervals[-1][1], interval[1])
            else:
                newIntervals.append(interval)
        
        return newIntervals

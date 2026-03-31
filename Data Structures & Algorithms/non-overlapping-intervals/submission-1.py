class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x:x[1])
        end = intervals[0][1]
        count = 1
        for x,y in intervals[1:]:
            if x>=end:
                count += 1
                end = y
        return len(intervals) - count        
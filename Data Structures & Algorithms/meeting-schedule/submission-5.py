"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)

        n = len(intervals)
        for i in range(1, n):
            prev = intervals[i-1]
            current = intervals[i]

            if prev.end > current.start:
                return False
        return True


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn) + O(n)[space]
        intervals.sort()
        result = []
        for x,y in intervals:
            if not result or result[-1][1]<x:
                result.append([x,y])
            else:
                result[-1][1] = max(result[-1][1], y)
        return result            
        
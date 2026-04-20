from heapq import heappush, heappop
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted([(q,i) for i, q in enumerate(queries)])
        result = [-1] * len(queries)
        min_heap = []
        for q, idx in sorted_queries:
            i=0
            while i<len(intervals) and intervals[i][0] <= q:
                l,r = intervals[i]
                heappush(min_heap, (r-l+1, r))
                i += 1
            while min_heap and min_heap[0][1] < q:
                heappop(min_heap)
            if min_heap:
                result[idx] = min_heap[0][0]
        return result



        